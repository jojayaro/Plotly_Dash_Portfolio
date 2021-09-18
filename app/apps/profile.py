from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
import pandas as pd
import plotly.graph_objects as go


CONTENT_STYLE = {
    "padding": "1rem 1rem",
}

profile_df = pd.read_csv("profile.csv")

d = {
    'Life': 'green',
    'Work': 'red',
    'Education': 'blue',
}

mapbox_access_token = open("mapbox").read()

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

def map_fig(df):
    
    dfmap = go.Figure()

    sub_list = df['Activity'].unique()
    for sub in sub_list:
        dfmap.add_trace(go.Scattermapbox(
            lat=df[df['Activity'] == sub]['Latitude'],
            lon=df[df['Activity'] == sub]['Longitude'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=10,
                color= d[sub]
            ),
            text=df[df['Activity'] == sub]['Description'],
            name=sub,
            #customdata=df[df['SUBSTANCE'] == sub]['LICENCE NUMBER'],
        ))

    dfmap.update_layout(
        height = 800,
        #width = 800,
        hovermode='closest',
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            pitch=0,
            center=go.layout.mapbox.Center(
                lat=22.5,
                lon=-34.5
            ),            
            zoom=1,
            style='dark'
        )
    )
    return dfmap

layout = html.Div([
        dbc.Row(
            dbc.Col(html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H2("Profile", className='card-title'),
                        ], className='card-body')
                ], className='card')
            ],style = CONTENT_STYLE)),
        ),
        dbc.Row(
            dbc.Col(html.Div([
                dbc.Card([
                    dbc.CardBody([
                            dcc.Graph(id = 'profile_map', figure = map_fig(profile_df)),
                        ], className='card-body')
                ], className='card')
            ],style = CONTENT_STYLE)),
        ),
])

