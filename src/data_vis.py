from collections import defaultdict

import pandas as pd
import plotly as py
import plotly.graph_objects as go


def get_year(release_date):
    if not isinstance(release_date, str):
        return None
    year_month_day = release_date.split('-')
    if len(year_month_day) != 3:
        return None
    year = int(year_month_day[0])
    return year


def visualize_num_movies_years(df):
    year = df['release_date'].apply(get_year)
    year_count = year.value_counts().sort_index()

    data = [go.Bar(name='movies/year', x=year_count.index, y=year_count.values)]
    layout = go.Layout(title='Numbers of movies per year')
    fig = go.Figure(data=data, layout=layout)
    return fig


def visualize_genres(df):
    genre_count = dict()
    for genre_list in df['genre_names']:
        for g in genre_list.strip('[]').split(','):
            g = g.strip()[1:-1]
            genre_count[g] = genre_count.get(g, 0) + 1
    genres, counts = list(zip(*genre_count.items()))
    data = [go.Pie(labels=genres, values=counts)]
    layout = go.Layout(
        title='Movies proportion base on genres'
    )
    fig = go.Figure(data=data, layout=layout)
    fig.update_traces(textposition ='inside',textinfo='percent+label')
    return fig


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

    return fig
