# BigData2020 Mobility Change Project

## Group Name

subwayNYC

## Project Participants

Bangwen Sun (bs3845)

Hang Dong (hd1191)

Yunxiao Shi (ys3404)

## Set up

### Python

#### Environment

```
jupyterlab==2.1.1
numpy==1.18.1
pandas==1.0.3
matplotlib==3.1.3
seaborn==0.10.0
folium==0.10.1
lxml==4.5.0
uszipcode==0.2.4
```

Using pip:

```bash
pip3 install -r requirements.txt # we suggest using python 3.6 or 3.7
```

Using [Conda](https://www.anaconda.com/):

```bash
conda create --name bigdta-py36 python=3.6 # use python 3.6
conda activate bigdta-py36
conda install -c conda-forge jupyterlab
conda install -c anaconda numpy
conda install -c anaconda pandas
conda install -c conda-forge matplotlib
conda install -c anaconda seaborn
conda install -c conda-forge folium
conda install -c anaconda lxml
pip install uszipcode
```

#### PySpark

on NYU@HPC DUMBO cluster

## Files

```./data_cleaning```

- ```./turnstile``` Turnstile data cleaning on HPC
- ```citibike_cleaning.ipynb``` Cleaning and visualizing CitiBike trip history data
- ```turnstile_cleaning.ipynb``` Cleaning turnstile data, deprecated, more as familiarization
- ```turnstile_cleaning_functions.ipynb``` Cleaning turnstile data for analysis, crawls data from MTA web site. Output cleaned turnstile counter difference data in 2019 and 2020.
- ```turnstile_locatin_integration.ipynb``` Integrate the result of ```turnstile_cleaning_functions.ipynb```, station location data ```geocoded_ca_unit.csv```, and NYC zip code and neighborhood data ```nyc_zipcode_neighborhood.csv```. Output stations defined by station name and lines with their location, zip code, and neighborhood.
- ```MTA_Bridge_and_Tunnel.ipynb``` Cleaning and analyzing MTA bridge and tunnel data

```./turnstile_flow_analysis```

- ```turnstile_plots.ipynb``` Aggregating and visualizing turnstile counter reading data, and station location data produced by ```turnstile_cleaning_functions.ipynb``` and ```turnstile_locatin_integration.ipynb```.

```./turnstile_neighborhood_analysis```



```./subway_tweets_analysis```



```./data```

- ```nyc_zipcode_neighborhood.csv``` NYC zip code, neighborhood, and borough data from [health.ny.gov](https://www.health.ny.gov/statistics/cancer/registry/appendix/neighborhoods.htm), missing zip codes manually added
- ```./turnstile```
  - ```geocoded_ca_unit.csv``` station location data by control area and remote unit
  -  ```turnstile_diffs_2019.csv.zip```, ```turnstile_diffs_2020.csv.zip```, ```turnstile_diffs_test.csv.zip``` cleaned turnstile counter reading data produced by ```turnstile_cleaning_functions.ipynb```
  - ```geocoded_station_lines.csv``` cleaned station location and neighborhood data produced by ```turnstile_locatin_integration.ipynb```
  - ...

- ```./citibike```
- ```./mta_bridge_and_tunnel```

## Contributing

1. Make a branch from `master` and add your changes:

```bash
git checkout master # switch to master branch
git pull origin master # sync up with remote
git checkout -b your_branch_name # make your new branch

# make changes
git add -u # add your changes
git commit -m "description of your changes"
git push origin your_branch_name
```

2. Using this branch, open a pull request on Github
