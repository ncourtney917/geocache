import dash
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import geocoder
g = geocoder.ip('me')

print(g.latlng)

dash_app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app = dash_app.server

dash_app.layout = html.Div([
    html.H1("Geocache Page"),
    html.H2(g.latlng)
])

if __name__ == '__main__':
    dash_app.run_server(debug=True)