import dash
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import geocoder

g = geocoder.ip('me')

dash_app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SIMPLEX])
app = dash_app.server


header_path = 'assets/geocache_header.png'
header_img = html.Img(src=header_path, className="fullscreen")

map_path = 'assets/bartholdi_map.png'
map_img = html.Img(src=map_path, className="fullscreen")
title = html.H1("Bartholdi's Bounty")
subtitle = html.P("GCHU783H - Traditional")
header = html.Div([title, subtitle], className="centered", style={"padding-top":"30px"})
cache_info_path = 'assets/cache_info.png'
cache_info = html.Img(src=cache_info_path, className="fullscreen")

main_buttons = html.Div([dbc.Button("Navigate", className="button-style"), dbc.Button("Log", className="button-style")], className="centered")



dash_app.layout = html.Div([
    header_img,
    map_img,
    header,
    cache_info
])





if __name__ == '__main__':
    dash_app.run_server(debug=True, )