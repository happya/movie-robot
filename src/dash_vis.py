#!/usr/bin/env python
# coding: utf-8

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly as py
import plotly.graph_objects as go
import pandas as pd

# init dash app
from src.data_vis import visualize_num_movies_years, visualize_genres, visualize_num_movies_companies

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def prepare_data(filename):
    if filename.endswith('.csv'):
        return pd.read_csv(filename)


def prepare_go_figs(filename):
    df = prepare_data(filename)
    go_figs = {
        'num-movie-years': visualize_num_movies_years(df),
        'visualize_genres': visualize_genres(df),
        'visualize_num_movies_companies': visualize_num_movies_companies(df)
    }

    return go_figs


def get_dcc_figs(go_figs):
    dcc_figs = []
    for gf in go_figs.items():
        dfig = dcc.Graph(id=gf[0], figure=gf[1])
        dcc_figs.append(dfig)
    return dcc_figs


def _head():
    return html.H1(children='Movie Robot', style={"text-align": "center"})


def run(dcc_figs):
    app.layout = html.Div(children=[_head()] + dcc_figs)


def main():
    go_figs = prepare_go_figs('../data/movies_cleaned.csv')
    dcc_figs = get_dcc_figs(go_figs)
    run(dcc_figs)


if __name__ == '__main__':
    main()
    app.run_server(port=8088, debug=True)
