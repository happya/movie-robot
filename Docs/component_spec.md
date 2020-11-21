# Movie-Robot Components Specification

### Component 1

- **Name**: `get_movie_info` 

- **Function**: show basic information of a movie

- **Input**: `movie_name(str)`
- **Output**: `movie_info(dict)`

Example:
```python
def get_movie_info(movie_name='Avatar'):
    return {'budget': 237000000, 
            'ratings': 7.2,
            'revenue': 2787965087,
            'runtime': 162,
            ...}
```

### Component 2

- **Name**: `show_stat_info`
- **Function**: Show statistic figures of movies with given specifications
- **Input**: 
  - `**specifications`: *e.g.* `{'lang':'', 'genre':'', 'year': xxxx})`
- **Output**: statistic figures


Example:
```python
def show_stat_information(genre='', language='', year=2017, ...):
    '''
    show statistic figures
    '''
```


### Component 3 

- **Name**: `get_top_k` 

- **Function**: Get top-k recommended movies based on given specifications

- **Input**: 
  - `**specifications`: `({'lang':'', 'genre':'', 'year': xxxx})`, 
  - `k`: `int`
  - `metrics`: `'rating' or 'popularity')`
- **Output**: 
  - `movies`: `List[Dict]`, `k` movies and their homepage links

Example

```python
def get_top_k(**specifications={'genre'='', 'language'=''}, k=10, metrics='popularity'):
  return ['movie_1': 'https//movie1',
          'movie_2': 'https//movie2',
          ...,
          'movie_k': 'https//moviek']

```

### Component 4 

- **Name**: `get_recommend` 

- **Function**: Get top-k recommended movies based on a given movie

- **Input**: 
  - `movie_name`: `str`, 
  - `k`: `int`
  - `metrics`: `'rating' or 'popularity')`
- **Output**: 
  - `movies`: `List[Dict]`, `k` movies and their homepage links

```python
def get_top_k(movie_name='Avatar', k=10, metrics='popularity'):
  return ['movie_1': 'https//movie1',
          'movie_2': 'https//movie2',
          ...,
          'movie_k': 'https//moviek']

```