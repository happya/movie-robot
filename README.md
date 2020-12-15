[![Build Status](https://travis-ci.com/happya/movie-robot.svg?branch=master)](https://travis-ci.com/github/happya/movie-robot/builds/207706144)
# Movie Robot

## Introduction

`TMDB` (The Movie DataBase) is a popular, user-editable database movies and TV shows.
The table have attribute like genre, homepage, movie_id, keywords, production_companies, country, release_date, language, vote_count...
With these information, we can provide many statistic information about the movies, and recommend the movies for the user base on the similarity.

Our project aims to provide inforamtion and insigts for movies based on different attributes and answer the question like:
- What is the top 10 Action movies in 2020?
- What is the top-10 movies similar to Avatar?
- Please recommend movies for me base on my appetite (Avatar).


...


## Team Member

**Chiao-Tung Yang**

**Weining Liang**

**Ya Yi**


## Data Sources

- [tmdb_5000_credits.csv](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv)
- [tmdb_5000_movies.csv](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

## Software dependencies and license information

**Programming language**

- Python (>=3.6)


**Python packages**

- pandas
- numpy
- matplotlib
- plotly
- dash


...

## Get setup and use the application

1. git clone https://github.com/happya/movie-robot.git
2. cd into the folder
3. install conda
4. conda create -n <env_name> python=3.8 -f envs.yml
5. run ./start.sh and open `localhost:8088` in your favorite browser
6. Explore and enjoy `movie-robot`
