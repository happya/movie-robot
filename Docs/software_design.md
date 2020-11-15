# Movie-Robot Design Doc

## 1. Requirement

- Users can get an overview of the basic statistics of all movies that can reveal underlying information and provide insights of the features (genres, languages, popularity, etc.) of movies.
- Users can get the most popular keywords of movies with given specifications.
- Users can get the recommended movies based on certain specifications (genre, release year, .etc).
- Users can get the recommended movies similar to a given movie.
- Users can get the links of all the recommended movies. 

## 2. Use Cases

### Use case 1: Show statistic figures with given specifications

```python
def show_information(genre='', language='', year=2017, ...):
    '''
    show statistic figures
    '''
```

### Use Case 2: Get top-k recommended movies based on given specifications

```python
def get_top_k(genre='', language='', k=10, criteria='popularity'):
  return list(movie_1, movie_2, ..., movie_k)

```

### Use Case 3: Get top-k recommended movies similar to a given movie


```python
def recommend_movie(movie='', k=10):
  return list(movie_1, movie_2, ..., movie_k)

```