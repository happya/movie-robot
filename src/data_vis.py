from collections import defaultdict

import plotly.express as px
import plotly.graph_objects as go


def visualize_num_movies_years(df):
    year_count = df['year'].value_counts().sort_index()

    data = [go.Bar(name='movies/year', x=year_count.index, y=year_count.values)]
    layout = go.Layout(title='Numbers of movies per year')
    fig = go.Figure(data=data, layout=layout)
    return fig


def get_genres_distribution(genre_col):
    genre_count = dict()
    for genre_list in genre_col:
        for g in genre_list.strip('[]').split(','):
            g = g.strip()[1:-1]
            genre_count[g] = genre_count.get(g, 0) + 1
    genres, counts = list(zip(*genre_count.items()))
    data = [go.Pie(labels=genres, values=counts)]
    return data


def visualize_num_movies_companies(df):
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


def data_url_link(df, title):
    link_col = df['homepage'][df['title'] == title]
    return link_col


def data_genre(df, year):
    if year == 'all':
        genre_col = df['genre_names']
    else:
        genre_col = df['genre_names'][df['year'] == int(year)]
    return get_genres_distribution(genre_col)


def data_language(df, year):
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
