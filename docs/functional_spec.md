# Movie-Robot Design Doc

## Background

Most people watch movies nowadays. However, it is very difficult for most people to watch all the movies that have been released. Sometimes, it is not easy to choose which movie to watch. There are too many characteristics for a certain movie. But if we can provide some useful statistic results based on distinct features of the movies, the users can have more ideas when choosing the movie to watch. Based on this, we can further recommend some movies to users that they will be more likely interested in and simultaneously provide the links of all the recommended movies to the user. The proposed Movie-Robot will be beneficial to both the users who enjoy watching movies and the production companies as well.

## Requirements

- Users can get detailed information of a movie.
- Users can get an overview of the basic statistics of all movies that can reveal underlying information and provide insights of the features (genres, languages, popularity, etc.) of movies.
- Users can get the most popular keywords of movies with given specifications.
- Users can get the recommended movies based on certain specifications (genre, release year, .etc).
- Users can get the recommended movies similar to a given movie.
- Users can get the links of all the recommended movies. 

## Use Cases

### Use case 1

Given a known movie title from the TMDB dataset, the movie-robot will return the basic information, like release date, production companies, genres, *.etc*.

### Use case 2

Given some specifications, like language, genre, release date, the movie-rebot will return the visualization results of the basic statistics based on these specifications. For example, given a year of 2010, it will return the statistic information of all movies released in year 2010, like the distribution of ratings, budgets, popularities, pie-chart of movies with different genres, produced by different companies, and so on so forth.  

### Use Case 3

Given some specifications, based on which the movie-robot will return the top-k recommended movies. The metrics can be ratings or popularity, and `k` is an integer number specified by the query user. For example, the user can query the top-10 Action movies released in year 2010 based on their recieved average ratings.

### Use Case 4 

Given a known movie, the movie-robot will return the top-10 movies that are similar to this movie.


## Data Sources

The Movie-Robot uses two datasets, which can be found [here](../README.md).

1.	tmdb_5000_credits.csv

This dataset contains information about movie ID, title, cast, and crew. Both the cast and crew fields are json format data including the general information about the actors, actresses, and the crew.

2.	tmdb_5000_movies.csv

This dataset has the information including budget, genres, homepage, movie ID, keywords, original language, overview, popularity, production companies, production countries, release date, revenue, runtime, spoken language, status, tagline, title, vote average, and vote count.

