#!/usr/bin/env python
# coding: utf-8
import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly as py
import plotly.graph_objects as go
import pandas as pd

# init dash app
from dash.dependencies import Input, Output

from src.data_vis import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})


def prepare_data(filename):
    if filename.endswith('.csv'):
        return pd.read_csv(filename)


data_path = os.path.abspath(os.path.join(__file__, '../../data/movies_cleaned.csv'))
df = prepare_data(data_path)


def prepare_go_figs():
    go_figs = {
        'movie_years': visualize_num_movies_years(df),
        'movie_companies': visualize_num_movies_companies(df),
    }

    return go_figs


def _get_drop_down(id, col):
    return dcc.Dropdown(
        id=id,
        options=[
            {'label': str(i), 'value': str(i)}
            for i in ['all'] + sorted(list(df[col].unique()), reverse=True)],
        value='all'
    )


def get_graphs_from_all_data(go_figs):
    return html.Div([
        html.Div([
            dcc.Graph(id='movie-years', figure=go_figs['movie_years']),
            dcc.Graph(id='movie-companies', figure=go_figs['movie_companies'])
        ], style={'display': 'flex', 'flex-direction': 'column'}),
        html.Div(
            [
                html.Div([
                    html.P('Please select year: (default by all)'),
                    _get_drop_down('genre-year-option', 'year')],
                    style={'display': 'inline-block', 'width': '49%'}),
                dcc.Graph(id='genre-year-pie'),
                html.Div([
                    html.P('Please select a year: (default by all)'),
                    _get_drop_down('lang-year-option', 'year')
                ], style={'display': 'inline-block', 'width': '49%'}),
                dcc.Graph(id='lang-year-pie')
            ],
            style={'display': 'inline-block', 'width': '100%'}
        ),

    ], style={'display': 'flex', 'width': '100%', 'margin': 'auto'})


def _update_graph_pie(selected, func, title):
    data = func(df, selected)
    layout = go.Layout(
        title=title + str(selected)
    )
    fig = go.Figure(data=data, layout=layout)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig


@app.callback(
    Output('lang-year-pie', 'figure'),
    Input('lang-year-option', 'value'))
def update_lang_year_graph(selected_year):
    title = 'Language of Movies in year ' + selected_year
    return _update_graph_pie(selected_year, data_language, title)


@app.callback(
    Output('genre-year-pie', 'figure'),
    Input('genre-year-option', 'value')
)
def update_genre_year_graph(selected_year):
    title = 'Language of Movies in year ' + selected_year
    return _update_graph_pie(selected_year, data_genre, title)
    data = data_(df, selected_year)
    layout = go.Layout(
        title='Language of Movies in year ' + selected_year
    )
    fig = go.Figure(data=data, layout=layout)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig


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
