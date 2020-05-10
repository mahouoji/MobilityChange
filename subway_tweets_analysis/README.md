## NYC Covid-19 Subway Tweets Analysis

Apart from the detailed analysis we did using turnstile and bridge-tunnel data, in this part we also considered the aspect of how people felt about the impact of Covid-19 on public transportation. Naturally a nice way to see into this would be to get an idea of what people are posting Twitter about this, and that's we did. Below outlines the things we looked at and how to adapt this part of code for your own use if you are inclined.

## Set-up and Things We Looked at

Due to the constraint of time and resources, also the restrictions of Twitter API, we pull down 6,866 tweets in the last 24 hours in the NYC region (geo-location filtering) and under the keywords of ```subway, covid, ridership, NYC, MTA```. Using this data, we investigated:

+ What are people's emotions in these tweets? (sentiment analysis) 

+ What are the popular hashtags in these tweets? (hashtag cloud)

+ Are there any tweets that attracted unusual attention? (tweets with lots of retweets)

+ How does people's emotions vary temporally?

## Usage and Requirements

1. Set up and obtain Twitter user access tokens following [this guide](https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a/obtaining-user-access-token). Put them in ```config.py```.

2. Install and set up [Elasticsearch](https://www.elastic.co/) and [Kibana](https://www.elastic.co/kibana) following [this guide](https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-logstash-and-kibana-elastic-stack-on-ubuntu-18-04).

3. ```pip install -r requirements.txt``` to install the required dependencies. 

4. Do ```python sentiment.py``` to start pulling down the tweets. You can specify your own filtering criteria in line #93-94 in ```sentiment.py``` where we set geolocations and keywords filtering. Of course alternatively you can use ```argparse``` to pass in those arguments by CLI.

5. Refer to (Kibana user guide)[https://www.elastic.co/guide/en/kibana/7.6/index.html] to customize your own visualizations.

## Summarized Conclusions (Things we looked at)

+ Positive and neutral tweets takes up the majority of people's tweets, with only 13.68% being negative tweets.

+ #Aline, #Fline, #Bline, etc are frequently present in people's tweets.

+ Not exactly under this volume of tweets, but subway incident reports tend to stand out.

+ Quite erratic. Does not exhibit a pattern.

You can refer to ```snapshots/``` for what the visualization analysis looks like. Note that it is taken from real-time streaming. 

## Disclaimer

If you encountered problems when trying to reproduce or adapt for your own use, please reach out to us. We can help.
