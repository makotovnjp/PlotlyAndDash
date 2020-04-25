# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np

app = dash.Dash()

# Creating Data
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app.layout = html.Div([dcc.Graph(id='scatterplot',
                       figure={'data': [go.Scatter(x=random_x, y=random_y, mode='markers')],
                               'layout': go.Layout(title='My layout')}
                                 ),
                       dcc.Graph(id='scatterplot2',
                       figure={'data': [go.Scatter(x=random_x, y=random_y, mode='markers')],
                               'layout': go.Layout(title='My layout')}
                                 ),

                       ])

if __name__ == '__main__':
    app.run_server(debug=True)