# -*- coding: utf-8 -*

# Initial version of sentiment.py

import json
import datetime
from dateutil.parser import parse
from http.client import IncompleteRead
import numpy as np
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch

# import twitter keys and tokens
from config import *

# create instance of elasticsearch
es = Elasticsearch()

# start = datetime.datetime(2020, 1, 1, 00, 00, 00)
# end = datetime.datetime(2020, 4, 30, 00, 00, 00)

class TweetStreamListener(StreamListener):

    # on success
    def on_data(self, data):
        # decode json
        dict_data = json.loads(data)
        # pass tweet into textblob
        tweet = TextBlob(dict_data["text"]) if 'text' in dict_data.keys() else None
        # output sentiment popularity
        # determine if sentiment is pos, neg or neutral
        if tweet:
            if tweet.sentiment.polarity < 0:
                sentiment = "negative"
            elif tweet.sentiment.polarity == 0:
                sentiment = "neural"
            else:
                sentiment = "positive"
            # output sentiment
            # print(parse(dict_data["created_at"]))
            # print(dict_data['text'], '\n')

        hashtags = ""
        if 'entities' in dict_data.keys():
            if len(dict_data['entities']['hashtags']) > 0:
                hashtags = dict_data['entities']['hashtags'][0]['text'].title()
            # else:
            #     hashtags = 'empty hashtags'
          

        # add text and sentiment info to elasticsearch
        es.index(index='nyc-subway', 
                doc_type='test-type', 
                body={
                    'author': dict_data['user']['screen_name'] if 'user' in dict_data.keys() else "",  
                    'followers': int(dict_data['user']['followers_count']) if 'user' in dict_data.keys() else -1, 
                    'date': parse(dict_data["created_at"]) if 'created_at' in dict_data.keys() else parse("Thu Jan 1 23:59:59 +0000 1970"), 
                    'message': dict_data['text'] if 'text' in dict_data.keys() else "", 
                    'hashtags': hashtags, 
                    'polarity': tweet.sentiment.polarity if tweet is not None else -2.0, 
                    'subjectivity': tweet.sentiment.subjectivity if tweet is not None else -2.0, 
                    'sentiment': sentiment if tweet is not None else -2.0,
                    # 'longitude': dict_data['geo']['coordinates'][1] if 'geo' in dict_data.keys() and dict_data['geo'] is not None else 0.0,
                    # 'latitude': dict_data['geo']['coordinates'][0] if 'geo' in dict_data.keys() and dict_data['geo'] is not None else 0.0
                    'location': dict_data['place']['full_name'] if 'place' in dict_data.keys() and dict_data['place'] is not None else "",
                    'longitude': dict_data['coordinates']['coordinates'][0] if 'coordinates' in dict_data.keys() and dict_data['coordinates'] is not None else 0.0,
                    'latitude': dict_data['coordinates']['coordinates'][1] if 'coordinates' in dict_data.keys() and dict_data['coordinates'] is not None else 0.0
                    })
        return True

    # on failure
    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # create instance of tweepy tweet stream listener
    listener = TweetStreamListener()

    # set twitter keys/tokens
    auth = OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    while True:
        try:
            # create instance of tweepy stream
            stream = Stream(auth, listener)
            # geolocation filtering restrict to tweets from NYC region
            stream.filter(languages=['en'], locations=[-74.1687,40.5722,-73.8062,40.9467])
            # keywords filtering for selected topics
            stream.filter(track=['subway','ridership','NYC','covid','MTA'])
        except IncompleteRead:
            continue
        except KeyboardInterrupt:
            stream.disconnect()
            break


