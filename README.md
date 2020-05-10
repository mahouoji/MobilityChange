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

### PySpark

on NYU@HPC DUMBO cluster

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
