"""
script name   : line_plotting.py
Functionality : Line plotting using python dash framework
Created on    : 23 SEP 2018
"""
__author__ = 'Ganesh'

# Global Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import random

app = dash.Dash()

x = list()
y = list()

for item in range(5):
    x.append(random.randint(1, 50))
    y.append(random.randint(60, 150))
print x, y

app.layout = html.Div(children=[
    html.H1(children='GK Dashboard'),
    dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x': x,
                 'y': y,
                 'type': 'line',
                 'name': 'Random Data'}
                ],
            'layout': {
                'title': 'Sensor board'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
