from collections import defaultdict

import plotly.express as px
import plotly.graph_objects as go
import heapq


def visualize_num_movies_years(df):
    '''
    Illustrate the figure of numbers of movies per year
    :param df: the processed data
    :return: the corresponding figure
    '''
    year_count = df['year'].value_counts().sort_index()

    data = [go.Bar(name='movies/year', x=year_count.index, y=year_count.values)]
    layout = go.Layout(title='Numbers of movies per year')
    fig = go.Figure(data=data, layout=layout)
    return fig


def get_genres_distribution(genre_col):
    '''
    Get the distribution for genres
    :param genre_col: the genre column
    :return: the corresponding data
    '''
    genre_count = dict()
    for genre_list in genre_col:
        for g in genre_list.strip('[]').split(','):
            g = g.strip()[1:-1]
            genre_count[g] = genre_count.get(g, 0) + 1
    genres, counts = list(zip(*genre_count.items()))
    data = [go.Pie(labels=genres, values=counts)]
    return data


def visualize_num_movies_companies(df):
    '''
    Illustrate the figure of numbers of movies made by different companies
    :param df: the processed data
    :return: the corresponding figure
    '''
    companies = df['company_name'].value_counts()

    data = [go.Bar(
        name='num_movies_made_by_companies',
        x=list(companies.index)[:20],
        y=list(companies.values)[:20], marker={
            "color": "orange",
            "line": {
                "width": 2,
                "color": "orange"
            }})]
    layout = go.Layout(title='Numbers of movies made by different companies')
    fig = go.Figure(data=data, layout=layout)
    fig.update_xaxes(tickangle=45)
    return fig


def visualize_num_movies_countries(df):
    '''
    Illustrate the figure of numbers of movies made by different countries
    :param df: the processed data
    :return: the corresponding figure
    '''
    countries = df['country_name'].value_counts()

    data = [go.Bar(
        name='num_movies_made_by_countries',
        x=list(countries.index)[:20],
        y=list(countries.values)[:20], marker={
            "color": "orange",
            "line": {
                "width": 2,
                "color": "orange"
            }})]
    layout = go.Layout(title='Numbers of movies made by different countries')
    fig = go.Figure(data=data, layout=layout)
    fig.update_xaxes(tickangle=45)
    return fig


def visualize_voting_range(df):
    '''
    Illustrate the vote average count figure
    :param df: the processed data
    :return: the corresponding figure
    '''
    fig = go.Figure(data=[
        go.Histogram(x=df['vote_average'])
    ])

    data = [go.Histogram(x=df['vote_average'])]
    layout = go.Layout(title='Vote average count')
    fig = go.Figure(data=data, layout=layout)
    return fig


def data_movie_info(df, title):
    '''
    Get the information for the specific movie
    :param df: the processed data
    :param title: the selected movie title
    :return: the corresponding result data
    '''
    info_table = df[df['title'] == title]
    return info_table


def data_genre(df, year):
    '''
    Get the genre distribution
    :param df: the processed data
    :param year: the selected year
    :return: the corresponding result data
    '''
    if year == 'all':
        genre_col = df['genre_names']
    else:
        genre_col = df['genre_names'][df['year'] == int(year)]
    return get_genres_distribution(genre_col)


def data_language(df, year):
    '''
    Get the language data for a certain year
    :param df: the processed data
    :param year: the selected year
    :return: the corresponding result data
    '''
    if year == 'all':
        language = df['lang'].value_counts()
        lang_abbr = df['lang_short'].value_counts()
    else:
        language = df['lang'][df['year'] == int(year)].value_counts()
        lang_abbr = df['lang_short'][df['year'] == int(year)].value_counts()
    lang = list(zip(language.index[:10], lang_abbr.index[:10]))
    data = [go.Pie(labels=['{}: {}'.format(a[1], a[0]) for a in lang],
                   values=language.values[:10])]
    return data


def recommend_k_movies_genre(df, genre, k):
    '''
    Get the recommended movies based on a selected genre
    :param df: the processed data
    :param genre: the selected genre
    :param k: the number we will get for the result
    :return: the corresponding result data
    '''
    # return list [(movie1, rate1), movie2, rate2), ...] size is k
    if len(df) == 0:
        raise ValueError('Empty data is not allowed.')

    if not isinstance(genre, str):
        raise TypeError('Genre type should be string.')

    heap = []
    for i in range(len(df)):
        genre_list = df.loc[i, 'genre_names']
        if genre not in genre_list:
            continue
        m_name = df.loc[i, 'title']
        m_rate = df.loc[i, 'vote_average']
        heapq.heappush(heap, (m_rate, m_name))
        if len(heap) > k:
            heapq.heappop(heap)

    rate_movie = {}
    while heap:
        s, m = heapq.heappop(heap)
        rate_movie[m] = s
    return rate_movie


def get_year(release_date):
    '''
    Get the year from a data
    :param release_date: the released data
    :return: its year
    '''
    if not isinstance(release_date, str):
        return -1
    year_month_day = release_date.split('-')
    if len(year_month_day) != 3:
        return -1
    year = int(year_month_day[0])
    return year


def recommend_k_movies_year(df, year, k):
    '''
    Get the recommended movies based on the selected year
    :param df: the processed data
    :param year: the selected year
    :param k: the number we will get for the result
    :return: the corresponding result data
    '''
    # return list [(movie1, rate1), movie2, rate2), ...] size is k
    if len(df) == 0:
        raise ValueError('Empty data is not allowed.')

    movies = df[['title', 'vote_average']][df['year'] == int(year)]
    movies_data = movies.to_dict('split')['data']
    movies_dict = {i[0]: i[1] for i in movies_data}
    k = k if len(movies_dict) >= k else len(movies_dict)
    return sorted(movies_dict.items(), key=lambda x: -x[1])[:k]
