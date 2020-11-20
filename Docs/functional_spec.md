# Movie-Robot Design Doc

## Background

Most people watch movies nowadays. However, it is very difficult for most people to watch all the movies that have been released. Sometimes, it is not easy to choose which movie to watch. There are too many characteristics for a certain movie. But if we can provide some useful statistic results based on distinct features of the movies, the users can have more ideas when choosing the movie to watch. Based on this, we can further recommend some movies to users that they will be more likely interested in and simultaneously provide the links of all the recommended movies to the user. The proposed Movie-Robot will be beneficial to both the users who enjoy watching movies and the production companies as well.

## Requirement

- Users can get an overview of the basic statistics of all movies that can reveal underlying information and provide insights of the features (genres, languages, popularity, etc.) of movies.
- Users can get the most popular keywords of movies with given specifications.
- Users can get the recommended movies based on certain specifications (genre, release year, .etc).
- Users can get the recommended movies similar to a given movie.
- Users can get the links of all the recommended movies. 

## Use Cases

### Use case 1: Show statistic figures with given specifications

### Use Case 2: Get top-k recommended movies based on given specifications

### Use Case 3: Get top-k recommended movies similar to a given movie


## Data Sources

The Movie-Robot uses two datasets, which can be found in README.md
1.	tmdb_5000_credits.csv
This dataset contains information about movie ID, title, cast, and crew. Both the cast and crew fields are json format data including the general information about the actors, actresses, and the crew.
2.	tmdb_5000_movies.csv
This dataset has the information including budget, genres, homepage, movie ID, keywords, original language, overview, popularity, production companies, production countries, release date, revenue, runtime, spoken language, status, tagline, title, vote average, and vote count.

