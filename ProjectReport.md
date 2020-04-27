# BigData2020 Project

## Group Name

subwayNYC

## Project Participants

Bangwen Sun (bs3845)

Hang Dong (hd1191)

Yunxiao Shi (ys3404)

## Project Description

In respond to the pandemic, mobility in cities changed drastically under administrative restriction and voluntary behavior change. Resent studies [1, 3] quantified state-level or country-level mobility change using mobility statistics. Within New York City, traffic volume and public transportation usage has dropped, while different neighborhoods may respond differently [2].

In this project we will use MTA turnstile data, along with other datasets, to analyze the mobility change in terms of subway ridership in different areas of NYC.

### Problems

- How does mobility change over time? How does stat-at-home policies affect the trends?
- Dose mobility change show different patterns in different areas?
- How does subway ridership correlate to other matrices such as confirmed cases?

### Approaches

We use MTA Turnstile Usage Data because it is updated frequently and has a granularity suitable for our analysis of daily mobility changes in small areas. We will first clean and process raw turnstile data into subway ridership by station per day. We may select those stations with higher number of traffic and compare the number after the outbreak with that in previous months or in previous years.  We can visualize ridership over time using line chart and see if the trend correspond to important dates regarding the pandemic. Our result may be used to validate the results of [1] and [3].

To demonstrate the mobility changes in different urban area, we will integrate ridership data and MTA Station Location data. Because the documentary format of station names may differ in these data sets, we will figure out the similarity of names using edit distance. We will visualize ridership and the percentage of ridership change using dot map for each staton and choropleth map for aggregated regions. The latter allows us to compare our result with other figures of different spacial granularity, for example, confirmed cases by zip code or borough. We will do spacial aggregation on stations and implement quad tree index.

Based on the result of the above steps, we might need to delve into more detailed information. For example, grouping subway ridership data by lines or time periods in one day. We may also refer to other datasets, such as MTA Fare Data for different card types, to see if we can have better understanding of the rider population. As complement to subway traffic, we might use data from other transportation systems like citibike and MTA bridge and tunnel usage. Since those data are aggregated and uploaded by various time span, we will need to aggregate turnstile data by week or month accordingly.

We will use Python and Jupyter Notebook in this project. We will use packages  such as NumPy, pandas, GeoPandas, Matplotlib, and seaborn.

## Data Cleaning and Integration

### Turnstile Data Preprocessing

Turnstile data contains 11 fields: 
C/A, UNIT, SCP, STATION, LINENAME, DIVISION, DATE, TIME, DESC, ENTRIES, EXITS

To summarize the ridership of each station for a certain time e.g. one week, four specified fields should be focused: 
STATION: Represents the station name the device is located at
DIVISION: Represents the Line originally the station belonged to BMT, IRT, or IND
ENTRIES: The cumulative entry register value for a device
EXITS: The cumulative exit register value for a device

Because two stations may have the same name in different transit agencies, (e.g. IND 103 St, IRT 103 St), station and division name should both be used as the primary key to define a specific station. Next, combine the records of ENTRIES and EXITS together and calculate the sum for each station. Thus, the ridership of each station in a period can be calculated.

Station GTFS Data Preprocessing

Station data contains 13 fields:
Station ID, Complex ID, GTFS Stop ID, Division, Line, Stop Name, Borough, Daytime Routes, Structure, GTFS Latitude, GTFS Longitude, North Direction Label, South Direction Label

Only station names and GTFS locations are useful for calculating the location. Some traffic hubs have several entrances for different lines, and their geographical positions are close. Thus, average values of latitude and longitude would be calculated to represent the location of these huge stations.

It still requires some processes before the integration of these two data sets because the syntax of station names might be different (e.g. Grand St, grand street). By translating station names to lower cases and conduct the inner join based on Division and Station names, the dataset containing stations with same name in two sets can be figured out. 

Next step will be calculating the similarity of station names using edit distance for these stations which cannot make a pair.

## List of Dataset

| Dataset                                                      | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [MTA Turnstile Usage Data](http://web.mta.info/developers/turnstile.html) | Weekly released cumulative entrance and exit count of each turnstile for each record datetime, also contains station name and line names. For each week, there is a CSV formatted text file, with header: <br />**C/A,UNIT,SCP,STATION,LINENAME,DIVISION,DATE,TIME,DESC,ENTRIES,EXITS**<br />C/A – The Control Area is the operator booth in a station. Some stations only have one operator booth. However, larger stations may have more than one.<br />UNIT – The Remote Unit, which is the collection of turnstiles. A station may have more than one Remote Unit.<br />SCP – The Subunit Channel Position represents the turnstile and the number used may repeat across stations. The **UNIT and SCP together is a unique identifier of a turnstile**.<br />STATION - Name of station, e.g. "59 ST"<br />LINENAME - Lines, e.g. "NQR456W"<br />DATE – The Date is the date of the recording with the format MM/DD/YYYY.<br />TIME – The Time is the time for a recording, with the format: HH:MM:SS.<br />DESC – The DESC is the type of event of the reading. **The turnstiles submit “Regular” readings every four hours.** They stagger the exact time of the readings across all the turnstiles and stations. Staggering the data submission times avoids having all the turnstiles update at simultaneously. “Recover Audit” designates scheduled readings taken after a communication outage. Other values such as “DoorClose” and “DoorOpen” represent unscheduled maintenance readings.<br />ENTRIES - The ENTRIES are a cumulative count of turnstile entrances. Note, the ENTRIES do not reset each day or for each recording period. **The turnstile entry count continues to increase until it reaches the device limit and then resets to zero.**<br />EXITS - The EXITS are a cumulative count of the turnstile exits. |
| [MTA Station Locations](http://web.mta.info/developers/data/nyct/subway/Stations.csv) | Latitude and longitude of subway stations, also contains stop name, line names, direction labels etc. |
| [Station Locations](https://github.com/chriswhong/nycturnstiles/blob/master/geocoded.csv) | Unofficial latitude and longitude of subway stations, updated on 4/23/2013.<br />Header: remote unit, control area, station, lines, division, latitude, longitude |
| [MTA Fare Data](http://web.mta.info/developers/fare.html)    | The number of MetroCard swipes made each week by customers entering each station of the New York City Subway, PATH, AirTrain JFK and the Roosevelt Island Tram, broken out to show the relative popularity of the various types of MetroCards. MTA New York City Transit posts the latest data every Saturday by 1 a.m., and the dates listed in the links reference the date the data is posted. The data in the files covers seven-day periods beginning on the Saturday two weeks prior to the posting date and ending on the following Friday. |
| [Hourly Traffic on MTA Bridges and Tunnels](https://data.ny.gov/Transportation/Hourly-Traffic-on-Metropolitan-Transportation-Auth/qzve-kjga) | The number of vehicles (including cars, buses, trucks and motorcycles) that pass through each of the bridges and tunnels operated by the MTA each hour of the day. The data is updated weekly. |
| [Daily Traffic on MTA Bridges and Tunnels](http://web.mta.info/developers/data/bandt/trafficdata.html) | The number of vehicles (including cars, buses, trucks and motorcycles) that pass through each of the nine bridges and tunnels operated by the MTA each day. XML formatted. Uploaded each week. |
| [FHV Base Aggregate Report](https://data.cityofnewyork.us/Transportation/FHV-Base-Aggregate-Report/2v9c-2k7f) | Monthly report including weekly total dispatched trips and unique dispatched vehicles by base tabulated from FHV Trip Record submissions made by bases. Note: The TLC publishes base trip record data as submitted by the bases, and we cannot guarantee or confirm their accuracy or completeness. Therefore, this may not represent the total amount of trips dispatched by all TLC-licensed bases. The TLC performs routine reviews of the records and takes enforcement actions when necessary to ensure, to the extent possible, complete and accurate information. |
| [Citi Bike Trip History](https://s3.amazonaws.com/tripdata/index.html) | Citi Bike trip data, with latitude and longitude of start and end station. Updated monthly. (-March 2020) |
| [NYC COVID-19 Data](https://github.com/nychealth/coronavirus-data) | NYC coronavirus dataassembled by the NYC Department of Health and Mental Hygiene. <br />boro.csv - rates of confirmed cases by NYC borough of residence.<br />tests-by-zcta.csv - cumulative test and test positive count of NYC residents by ZIP code |
|                                                              |                                                              |

## Reference

1. Assessing changes in commuting and individual mobility in major metropolitan areas in the United States during the COVID-19 outbreak. ([link](https://www.networkscienceinstitute.org/publications/assessing-changes-in-commuting-and-individual-mobility-in-major-metropolitan-areas-in-the-united-states-during-the-covid-19-outbreak))

2. They Can’t Afford to Quarantine. So They Brave the Subway. ([link](https://www.nytimes.com/2020/03/30/nyregion/coronavirus-mta-subway-riders.html))

3. Mobility Changes in Response to COVID-19 ([link]( https://arxiv.org/pdf/2003.14228.pdf)).

4. Pass-Join: A Partition-based Method for Similarity Joins ([link](http://vldb.org/pvldb/vol5/p253_guoliangli_vldb2012.pdf))

5. Google COVID-19 Community Mobility Reports: Anonymization Process Description (version 1.0) ([link](https://arxiv.org/pdf/2004.04145.pdf))
