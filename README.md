# BigData2020 Project

## Group Name

tbd...

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

We use MTA Turnstile Usage Data because it is updated frequently and has a granularity suitable for our analysis of daily mobility changes in small areas. We will first clean and process raw turnstile data into subway ridership by station per day. We may select those stations with higher number of traffic and compare the number after the outbreak with that in previous months or in previous years.  We can visualize ridership over time using line chart and see if the trend correspond to important dates.

To demonstrate the mobility changes in different urban area, we will integrate ridership data and MTA Station Location data. Because the documentary format of station names may differ in these data sets, we will figure out the similarity of names using edit distance. We will visualize ridership and the percentage of ridership change using dot map for each staton and choropleth map for aggregated regions. The latter allows us to compare our result with other data sources in different spacial granularity, for example confirmed cases by zip code or by borough. We will do spacial aggregation on stations and implement quad tree index.

We will use Python numpy and pandas for data processing, matplotlib and seaborn for visualization. (?)

...

## List of Dataset

| Dataset                                                      | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [MTA Turnstile Usage Data](http://web.mta.info/developers/turnstile.html) | Weekly released cumulative entrance and exit count of each turnstile for each record datetime, also contains station name and line names. For each week, there is a CSV formatted text file, with header: <br />**C/A,UNIT,SCP,STATION,LINENAME,DIVISION,DATE,TIME,DESC,ENTRIES,EXITS**<br />C/A – The Control Area is the operator booth in a station. Some stations only have one operator booth. However, larger stations may have more than one.<br />UNIT – The Remote Unit, which is the collection of turnstiles. A station may have more than one Remote Unit.<br />SCP – The Subunit Channel Position represents the turnstile and the number used may repeat across stations. The **UNIT and SCP together is a unique identifier of a turnstile**.<br />STATION - Name of station, e.g. "59 ST"<br />LINENAME - Lines, e.g. "NQR456W"<br />DATE – The Date is the date of the recording with the format MM/DD/YYYY.<br />TIME – The Time is the time for a recording, with the format: HH:MM:SS.<br />DESC – The DESC is the type of event of the reading. **The turnstiles submit “Regular” readings every four hours.** They stagger the exact time of the readings across all the turnstiles and stations. Staggering the data submission times avoids having all the turnstiles update at simultaneously. “Recover Audit” designates scheduled readings taken after a communication outage. Other values such as “DoorClose” and “DoorOpen” represent unscheduled maintenance readings.<br />ENTRIES - The ENTRIES are a cumulative count of turnstile entrances. Note, the ENTRIES do not reset each day or for each recording period. **The turnstile entry count continues to increase until it reaches the device limit and then resets to zero.**<br />EXITS - The EXITS are a cumulative count of the turnstile exits. |
| [MTA Station Locations](http://web.mta.info/developers/data/nyct/subway/Stations.csv) | Latitude and longitude of subway stations, also contains stop name, line names, direction labels etc. |
| [NYTimes Confirmed Cases](https://github.com/nytimes/covid-19-data) |                                                              |
|                                                              |                                                              |

## Reference

1. Assessing changes in commuting and individual mobility in major metropolitan areas in the United States during the COVID-19 outbreak. ([link](https://www.networkscienceinstitute.org/publications/assessing-changes-in-commuting-and-individual-mobility-in-major-metropolitan-areas-in-the-united-states-during-the-covid-19-outbreak))

2. They Can’t Afford to Quarantine. So They Brave the Subway. ([link](https://www.nytimes.com/2020/03/30/nyregion/coronavirus-mta-subway-riders.html))

3. Mobility Changes in Response to COVID-19 ([link]( https://arxiv.org/pdf/2003.14228.pdf)).

4. Pass-Join: A Partition-based Method for Similarity Joins ([link](http://vldb.org/pvldb/vol5/p253_guoliangli_vldb2012.pdf))

5. Google COVID-19 Community Mobility Reports: Anonymization Process Description (version 1.0) ([link](https://arxiv.org/pdf/2004.04145.pdf))
