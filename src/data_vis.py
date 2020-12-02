import pandas as pd
import plotly as py
import plotly.graph_objects as go





def get_year(release_date):
    if not isinstance(release_date, str):
        return -1
    year_month_day = release_date.split('-')
    if len(year_month_day) != 3:
        return -1
    year = int(year_month_day[0])
    return year


def visualize_num_movies_years(df):
    year_count = {}
    for i in range(len(df)):
        y = df.loc[i, 'release_date']
        y = get_year(y)
        if y == -1:
            continue
        year_count.setdefault(y, 0)
        year_count[y] += 1

    year_count = sorted(year_count.items(), key=lambda x: x[0])
    years = [y for y, c in year_count]
    counts = [c for y, c in year_count]

    fig = go.Figure(data=[
        go.Bar(name='movies/year', x=years, y=counts)
    ])

    # Change the bar mode
    fig.update_layout(barmode='group')
    # fig.show()

    data = [go.Bar(name='movies/year', x=years, y=counts)]
    layout = go.Layout(title='Numbers of movies per year')
    fig = go.Figure(data=data, layout=layout)
    # py.offline.plot(fig, filename='numbers_of_movies_per_year.html')
    return fig


def visualize_genres(df):
    genre_count = {}
    for i in range(len(df)):
        genre_list = df.loc[i, 'genre_names']
        for g in genre_list:
            genre_count.setdefault(g, 0)
            genre_count[g] += 1

    genres = list(genre_count.keys())
    counts = list(genre_count.values())

    fig = go.Figure(data=[
        go.Pie(labels=genres, values=counts)
    ])

    fig.update_layout(title_text='Genres')

    data = [go.Pie(labels=genres, values=counts)]
    layout = go.Layout(title='Movies proportion base on genres')
    fig = go.Figure(data=data, layout=layout)
    return fig


def visualize_num_movies_companies(df):
    company_count = {}
    for i in range(len(df)):
        company = df.loc[i, 'company_name']
        company_count.setdefault(company, 0)
        company_count[company] += 1

    companies = list(company_count.keys())
    counts = list(company_count.values())

    data = [go.Bar(name='num_movies_made_by_companies', x=companies, y=counts, marker={
        "color": "orange",
        "line": {
            "width": 2,
            "color": "orange"
        }})]
    layout = go.Layout(title='Numbers of movies made by different companies')
    fig = go.Figure(data=data, layout=layout)

    return fig
