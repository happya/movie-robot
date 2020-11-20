# Movie-Robot Components Specification

### Component 1

What it does: Show statistic figures with given specifications
Input:
Output:

```python
def show_information(genre='', language='', year=2017, ...):
    '''
    show statistic figures
    '''
```

### Component 2 

What it does: Get top-k recommended movies based on given specifications
Input:
Output:

```python
def get_top_k(genre='', language='', k=10, criteria='popularity'):
  return list(movie_1, movie_2, ..., movie_k)

```

### Component 3 

What it does: Get top-k recommended movies similar to a given movie
Input:
Output:

```python
def recommend_movie(movie='', k=10):
  return list(movie_1, movie_2, ..., movie_k)

```