#!/usr/bin/env python
# coding: utf-8
import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import plotly as py
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# init dash app
from dash.dependencies import Input, Output

from src.data_vis import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})

def prepare_data(filename):
    '''
    Read the csv file to our format
    :param filename: the name of the input data file
    :return: pd.read_csv
    '''
    if filename.endswith('.csv'):
        return pd.read_csv(filename)


data_path = os.path.abspath(os.path.join(__file__, '../../data/movies_cleaned.csv'))
df = prepare_data(data_path)


def prepare_go_figs():
    '''
    Illustrate the static figures on the webpage
    :return: go_figs
    '''
    go_figs = {
        'movie_years': visualize_num_movies_years(df),
        'movie_companies': visualize_num_movies_companies(df),
        'movie_countries': visualize_num_movies_countries(df),
        'movie_votes': visualize_voting_range(df),
    }

    return go_figs


def _get_drop_down(id, col):
    '''
    Drop_down menu for the pie chart
    :param id: the object id
    :param col: the column name
    :return: the dash component for dropdown menu
    '''
    return dcc.Dropdown(
        id=id,
        options=[
            {'label': str(i), 'value': str(i)}
            for i in ['all'] + sorted(list(df[col].unique()), reverse=True)],
        value='all'
    )


def _get_drop_down_title(id, col):
    '''
    Drop_down menu for movie information
    :param id: the object id
    :param col: the column name
    :return: the dash component for dropdown menu
    '''
    return dcc.Dropdown(
        id=id,
        options=[
            {'label': str(i), 'value': str(i)}
            for i in sorted(list(df[col].unique()), reverse=False)
        ],
    )


def _get_drop_down_genres(id):
    '''
    Drop_down menu for recommendation system-genre
    :param id: the object id
    :return: the dash component for dropdown menu
    '''
    return dcc.Dropdown(
        id=id,
        options=[
            {'label': str(i), 'value': str(i)}
            for i in sorted(list(['Foreign', 'Horror', 'Science Fiction',
                                  'Thriller', 'Comedy', 'Drama', 'Western', 'Adventure',
                                  'Family', 'Romance', 'Mystery', 'Fantasy', 'Music', 'War',
                                  'History', 'Action', 'Animation', 'Documentary', 'TV Movie',
                                  'Crime']), reverse=False)
        ],
    )


def _get_drop_down_year(id, col):
    '''
    Drop_down menu for recommendation system-year
    :param id: the object id
    :param col: the column name
    :return: the dash component for dropdown menu
    '''
    return dcc.Dropdown(
        id=id,
        options=[
            {'label': str(i), 'value': str(i)}
            for i in sorted(list(df[col].unique()), reverse=True)],
    )


def geo_graph():
    '''
    Illustrate the geographic figure
    :return: fig
    '''
    country = pd.DataFrame(df['country_name'].value_counts().reset_index().values,
                           columns=['country', 'total'])
    # country = country[country['total'] > 0]
    data = go.Choropleth(
        locationmode='country names',
        z=np.log10(country['total'].to_list()),
        locations=country['country'],
        text=country['country'] + ': ' + country['total'].apply(str),
        colorscale='Blues',
        colorbar=dict(title='# movies',
                      tickvals=[0, 1, 2, 3, 3.477],
                      ticktext=['1', '10', '100', '1000', '3000'])

    )
    layout = go.Layout(title='Movies Produced by Countries')
    fig = go.Figure(data=data, layout=layout)
    return fig


def get_graphs_from_all_data(go_figs):
    '''
    The main layout for our homepage
    :param go_figs: the figures to be shown on the page
    :return: html.Div component
    '''
    return html.Div([
        dcc.Tabs([
            dcc.Tab(label='General', children=[

                # general information of a movie
                html.H2('General information of a movie'),
                html.Div([
                    html.Div([
                        html.P('Please select a movie name to review its introduction'),
                        _get_drop_down_title('movie-title-select-info', 'title')],
                        style={'display': 'inline-block', 'width': '49%'}),
                    dt.DataTable(id='movie-info-table',
                                 columns=[{"name": i, "id": i} for i in
                                          ["homepage", "company_name", "release_date", "genre_names", "vote_average"]],
                                 ),
                ], style={'width': '80%', 'margin': '20px auto'}),

                # distribution charts
                html.H2('Distribution of Movie Information'),
                html.Div([

                    html.Div([
                        dcc.Graph(id='movie-years', figure=go_figs['movie_years']),
                        dcc.Graph(id='movie-companies', figure=go_figs['movie_companies']),
                    ], style={'display': 'flex', 'flex-direction': 'column'}),
                    html.Div([
                        dcc.Graph(id='movie-countries', figure=go_figs['movie_countries']),
                        dcc.Graph(id='movie-votes', figure=go_figs['movie_votes']),
                    ])
                ], style={'display': 'flex', 'flex-direction': 'column'}),

                # pie charts
                html.H2('Pie Chart of Movie Genres and Languages'),
                html.Div([
                    html.Div([
                        html.P('Please select year: (default by all)'),
                        _get_drop_down('genre-year-option', 'year'),
                        dcc.Graph(id='genre-year-pie')
                    ], style={'display': 'flex', 'flex-direction': 'column', 'width': '49%'}),
                    html.Div([
                        html.P('Please select a year: (default by all)'),
                        _get_drop_down('lang-year-option', 'year'),
                        dcc.Graph(id='lang-year-pie'),
                    ], style={'display': 'flex', 'flex-direction': 'column', 'width': '49%'}),

                ], style={'display': 'flex', 'width': '100%', 'margin': '20px auto'}),

                # geograph
                html.H2('Geograph of Movie Production Countries'),
                html.Div([
                    dcc.Graph(id='geo-movie-countries', figure=geo_graph())
                ], style={'display': 'flex', 'width': '100%', 'margin': 'auto'}
                )]
                    ),
            dcc.Tab(label='Recommendation', children=[
                # Recommend top-10 movies base on genre and vote_average
                html.H2('Recommend top-10 movies based on genre and vote_average'),
                html.Div([
                    html.Div([
                        html.P('Please select a desired genre to get the recommendations'),
                        _get_drop_down_genres('recommend-genre-vote-input')
                    ],
                        style={'display': 'inline-block', 'width': '49%', 'margin': '20px auto'}),
                    dt.DataTable(id='recommend-genre-vote-output',
                                 columns=[{'name': i, 'id': i} for i in ["movie", 'rating']],
                                 style_cell={'textAlign': 'center'}),
                ], style={'width': '80%', 'margin': '20px auto'}),
                # Recommend top-10 movies base on year and vote_average
                html.H2('Recommend top-10 movies based on year and vote_average'),
                html.Div([
                    html.Div([
                        html.P('Please select a specific year to get the recommendations'),
                        _get_drop_down_year('recommend-genre-year-input', 'year')
                    ],
                        style={'display': 'inline-block', 'width': '49%', 'margin': '20px auto'}),
                    dt.DataTable(id='recommend-genre-year-output',
                                 columns=[{'name': i, 'id': i} for i in ["movie", 'rating']],
                                 style_cell={'textAlign': 'center'}
                                 ),
                ], style={'width': '80%', 'margin': '20px auto'})

            ]
                    )
        ])
    ], style={'width': '80%', 'margin': '20px auto'})


def _update_graph_pie(selected, func, title):
    '''
    Update the pie chart
    :param selected: the selected year/language
    :param func: the function to be called in data_vis.py
    :param title: the selected title
    :return: fig
    '''
    data = func(df, selected)
    layout = go.Layout(
        title=title
    )
    fig = go.Figure(data=data, layout=layout)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig


@app.callback(
    Output('recommend-genre-vote-output', 'data'),
    Input('recommend-genre-vote-input', 'value'))
def update_genre_recommend(selected_genre):
    '''
    Update the recommended movies results
    :param selected_genre: the selected genre
    :return: result table
    '''
    genre_string = str(selected_genre)
    dff = recommend_k_movies_genre(df, genre_string.lower(), 10)
    sorted_df = sorted(dff.items(), key=lambda x: -x[1])
    return [{"movie": i[0], "rating": i[1]} for i in sorted_df]
    # return html.Ul([html.Li(x) for x in dff])


@app.callback(
    Output('recommend-genre-year-output', 'data'),
    Input('recommend-genre-year-input', 'value'))
def update_genre_recommend(selected_year):
    '''
    Update the recommended movies results
    :param selected_year: the selected year
    :return: result table
    '''
    year = 1000
    if isinstance(selected_year, str):
        year = int(selected_year)
    dff = recommend_k_movies_year(df, year, 10)
    return [{"movie": i[0], "rating": i[1]} for i in dff]
    # return html.Ul([html.Li(x) for x in dff])


@app.callback(
    Output('movie-info-table', 'data'),
    Input('movie-title-select-info', 'value'))
def update_movie_info(selected_title):
    '''
    Update the movie information table
    :param selected_title: the selected title of the movie
    :return: the data to be shown in the table
    '''
    dff = data_movie_info(df, selected_title)
    return dff.to_dict('records')


@app.callback(
    Output('lang-year-pie', 'figure'),
    Input('lang-year-option', 'value'))
def update_lang_year_graph(selected_year):
    '''
    Update the language_year_chart
    :param selected_year: the selected year
    :return: the corresponding figure
    '''
    title = 'Language of Movies in year ' + selected_year
    return _update_graph_pie(selected_year, data_language, title)


@app.callback(
    Output('genre-year-pie', 'figure'),
    Input('genre-year-option', 'value')
)
def update_genre_year_graph(selected_year):
    '''
    Update the genre_year_chart
    :param selected_year: the selected year
    :return: the corresponding figure
    '''
    title = 'Genre of Movies in year ' + selected_year
    return _update_graph_pie(selected_year, data_genre, title)


def _head():
    return html.H1(children='Movie Robot', style={"text-align": "center"})


def run(dcc_figs):
    app.layout = html.Div(
        [
            _head(),
            dcc_figs
        ]
    )


def main():
    go_figs = prepare_go_figs()
    dcc_figs = get_graphs_from_all_data(go_figs)
    run(dcc_figs)


if __name__ == '__main__':
    main()
    app.run_server(port=8088, debug=True)
