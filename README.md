[![Build Status](https://travis-ci.com/happya/movie-robot.svg?branch=master)](https://travis-ci.com/github/happya/movie-robot/builds/207706144)

<img src="https://github.com/happya/movie-robot/blob/master/demo/icon.png" width=15% height=15%>

# Movie Robot


## Background

For people who love watching movie may want to ask questions like:
- How can we have a quick review for a selected movie?
- How can we get insightful information from thousands of movies?
- How can we quickly get some recommendation movies?

Our Movie Robot's goal is to provide a useful tool to solve these issues.

## Introduction

`TMDB` (The Movie DataBase) is a popular, user-editable database movies and TV shows.
The table have attribute like genre, homepage, movie_id, keywords, production_companies, country, release_date, language, vote_count...
With these information, we can provide many statistic information about the movies, and recommend the movies for the user base on the similarity.

Our project aims to provide inforamtion and insigts for movies based on different attributes and answer the question like:
- What is the top 10 Action movies in 2020?
- What is the top-10 movies similar to Avatar?
- Please recommend movies for me base on my appetite (Avatar).



## Team Member

**Chiao-Tung Yang**

**Wei-Ning Liang**

**Ya Yi**


## Data Sources

- [tmdb_5000_credits.csv](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv)
- [tmdb_5000_movies.csv](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

## Software dependencies and license information

**Programming language**

- Python (>=3.6)


**Python packages**

- pandas==1.1.5
- numpy==1.19.4
- plotly==4.14.1
- dash==1.18.1
- dash-core-components==1.14.1
- dash-html-components==1.1.1
- dash-renderer==1.8.3
- dash-table==4.11.1

...

## Directory Structure
```
movie-robot
    ├── LICENSE
    ├── README.md
    ├── data
    │   └── movies_cleaned.csv
    ├── demo  
    │   ├── Layout.png   
    │   └── Movie Robot Demo.mp4
    ├── docs
    │   ├── CSE583-Final Presentation.pptx
    │   ├── component_spec.md
    │   └── functional_spec.md
    ├── example
    │   ├── dash_vis.ipynb
    │   └── data_cleaning.ipynb
    ├── src
    │   ├── __init__.py
    │   ├── dash_vis.py
    │   └── data_vis.py
    ├── test
    │   ├── __init__.py
    │   └── test.py
    ├── requirements.txt
    ├── data_cleaning.ipynb
    ├── envs.yml
    └── star.sh
```

## Get setup and use the application

1. git clone https://github.com/happya/movie-robot.git
2. cd into the folder
3. You can either use `conda` or `pip` to setup your python environment:
    a. If you are using `conda`:
    ```bash
    # install conda
    # create environments based on the envs.yaml
    conda create -n <env_name> python=3.8 -f envs.yml
   ```
   b. If you are using `pip`:
   ```bash
   pip install requirments.txt -r
   ```
5. run ./start.sh and open `localhost:8088` in your favorite browser (Normally it will pop out automatically in your default browser)
6. Explore and enjoy `movie-robot`
## DEMO
![Demo](./demo/Movie Robot Demo.mp4)
## Movie Robot Homepage Preview
<img src="https://github.com/happya/movie-robot/blob/master/demo/Layout.png" width=85% height=85%>

