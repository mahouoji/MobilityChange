# BigData2020 Project

## Group Name

subwayNYC

## Project Participants

Bangwen Sun (bs3845)

Hang Dong (hd1191)

Yunxiao Shi (ys3404)

## Set up

### Python

Using [Conda](https://www.anaconda.com/):

```bash
conda create --name bigdta-py36 python=3.6 
conda activate bigdta-py36
conda install -c conda-forge jupyterlab
conda install -c anaconda numpy
conda install -c anaconda pandas
conda install -c conda-forge matplotlib
conda install -c anaconda seaborn
conda install -c conda-forge folium
```

### PySpark

...

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

