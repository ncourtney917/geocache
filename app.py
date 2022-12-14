import dash
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import geocoder
import folium

g = geocoder.ip('me')

dash_app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SIMPLEX])
app = dash_app.server


header_path = 'assets/geocache_header.png'
header_img = html.Img(src=header_path, className="fullscreen")

map_path = 'assets/map_with_marker.png'
map_img = html.Img(src=map_path, className="fullscreen", id="map-img")
title = html.H1("Bartholdi's Bounty")
subtitle = html.P("GCHU783H - Traditional")
header = html.Div([title, subtitle], className="centered", style={"padding-top":"30px"})
cache_info_path = 'assets/cache_info.png'
cache_info = html.Img(src=cache_info_path, className="fullscreen")

main_buttons = html.Div([dbc.Button("Navigate", className="button-style"), dbc.Button("Log", className="button-style")], className="centered")

hint_message = html.Div(
    [
    html.Button("Hint", className="halfscreen-buttons", id="hint-button"),
    html.Button("Message", className="halfscreen-buttons", id="message-button")
    ]
)

description_icon_path = 'assets/description_icon.png'
description_icon = html.Img(src=description_icon_path, className="icon-background")

description = html.Button(
    [
        description_icon,
        html.Div([
            html.P("Description", className="button-title"), 
            html.P("Bartholdi Park was named after...", className="button-subtitle")
        ], className="stack")
    ],
    className="fullscreen long-button flex", style={"margin-top":"20px"},
    id="description-button"
)

cache_bottom_path = 'assets/cache_bottom.png'
cache_bottom = html.Img(src=cache_bottom_path, className="fullscreen")

hint_modal = dbc.Modal(
    [
        dbc.ModalHeader(html.H2("Hint")),
        dbc.ModalBody("If you get weary, take a seat and rest for a minute.", style={"white-space": "pre-line"})
    ],
    is_open=False,
    className="modal-shift",
    id="hint-modal"
)

message_modal = dbc.Modal(
    [
        dbc.ModalHeader(html.H2("Messages")),
        dbc.ModalBody("Messages unavailable at this time. Please try again later.", style={"white-space": "pre-line"})
    ],
    is_open=False,
    className="modal-shift",
    id="message-modal"
)

description_modal = dbc.Modal(
    [
        dbc.ModalHeader(html.H2("Description")),
        dbc.ModalBody(
            """
                Bartholdi Park was named after French Sculptor Fr??d??ric Auguste Bartholdi who designed the fountain that sits in the middle of the park. The United States government bought the fountain from Bartholdi for $6,000 in 1877, a few years before Bartholdi designed his most famous work, the Statue of Liberty.
                
                The park was renovated in 2016 as a Sustainable SITES Initiative project, which emphasizes sustainable gardening in 5 key areas: water, plants, soil, materials, and human health. Rain gardens capture 100% of rainfall on the site, up to 4,000 cubic feet at a time, equivalent to 256 bathtubs of water.

                Learn more about the sustainability effort at:

                usbg.gov/bartholdi-fountain-and-gardens
            """, style={"white-space": "pre-line"}
)
    ],
    is_open=False,
    className="modal-shift",
    id="description-modal"
)

# Create Google Maps html file of Bartholdi
coords = [38.887012, -77.012786]
name= "Google Sat"
sat =  "https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}&hl=en"
m = folium.Map(location=coords, tiles=sat, zoom_start=17, max_zoom=20, attr="Google")
icon="cube"
icon = folium.Icon(icon=icon, prefix="fa", color="darkgreen")

# Add marker for cache location
marker = folium.Marker(
    coords,
    icon=icon,
).add_to(m)
m.save("assets/geocache_map.html")

map_modal = dbc.Modal(
    [
        dbc.ModalHeader(html.H2("Bartholdi's Bounty", className="centered")),
        dbc.ModalBody(id="map-card")
    ],
    is_open=False,
    fullscreen=True,
    id="map-modal"
)


@dash_app.callback(
    Output("hint-modal", "is_open"),
    Input("hint-button", "n_clicks"),
    prevent_initial_call=True
)
def open_hint(n):
    """Button to open Hint modal"""
    if n:
        return True
    return False


@dash_app.callback(
    Output("map-modal", "is_open"),
    Output("map-card", "children"),
    Input("map-img", "n_clicks"),
    prevent_initial_call=True
)
def open_map(n):
    """Button to open Map modal with map html from assets folder"""
    if n:
        map = html.Iframe(src="assets/geocache_map.html", style={"height": "100%", "width": "100%"})
        return True, map
    return False, []


@dash_app.callback(
    Output("description-modal", "is_open"),
    Input("description-button", "n_clicks"),
    prevent_initial_call=True
)
def open_description(n):
    """Button to open Description modal"""
    if n:
        return True
    return False


@dash_app.callback(
    Output("message-modal", "is_open"),
    Input("message-button", "n_clicks"),
    prevent_initial_call=True
)
def open_message(n):
    """Button to open Message modal"""
    if n:
        return True
    return False

# Create full app layout
dash_app.layout = html.Div([
    header_img,
    map_img,
    header,
    cache_info,
    hint_message,
    hint_modal,
    message_modal,
    description,
    description_modal,
    cache_bottom,
    map_modal
])





if __name__ == '__main__':
    dash_app.run_server(debug=True, )