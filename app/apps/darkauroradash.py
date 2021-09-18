# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import urllib, json
from plotly.subplots import make_subplots
from skimage import io
import datetime

from app import app

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

#server = app.server

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

CONTENT_STYLE = {
    "padding": "1rem 1rem",
}

#Functions
def magdf():
    urlmag2h = 'https://services.swpc.noaa.gov/products/solar-wind/mag-2-hour.json'
    responsemag2h = urllib.request.urlopen(urlmag2h)
    datamag2h = json.loads(responsemag2h.read().decode())
    dfmag2h = pd.DataFrame(datamag2h)
    dfmag2h.columns = dfmag2h.iloc[0]
    dfmag2h = dfmag2h[1:]
    dfmag2h_1 = dfmag2h[['time_tag','bt','bz_gsm']]
    dfmag2h_1['time_tag'] = pd.to_datetime(dfmag2h_1['time_tag'])
    dfmag2h_1['bt'] = dfmag2h_1['bt'].astype(float)
    dfmag2h_1['bz_gsm'] = dfmag2h_1['bz_gsm'].astype(float)
    return dfmag2h_1

def plasmadf():
    urlplasma2h = 'https://services.swpc.noaa.gov/products/solar-wind/plasma-2-hour.json'
    responseplasma2h = urllib.request.urlopen(urlplasma2h)
    dataplasma2h = json.loads(responseplasma2h.read().decode())
    dfp2h = pd.DataFrame(dataplasma2h)
    dfp2h.columns = dfp2h.iloc[0]
    dfp2h = dfp2h[1:]
    dfp2h_1 = dfp2h[['time_tag','density','speed','temperature']]
    dfp2h_1['time_tag'] = pd.to_datetime(dfp2h_1['time_tag'])
    dfp2h_1['density'] = dfp2h_1['density'].astype(float)
    dfp2h_1['speed'] = dfp2h_1['speed'].astype(float)
    dfp2h_1['temperature'] = dfp2h_1['temperature'].astype(float)
    return dfp2h_1

#Figures
def mag_fig(dfmag2h_1,dfp2h_1):
    figsw2h = make_subplots(rows=4, cols=1)
    figsw2h.add_trace(go.Scatter(x=dfmag2h_1['time_tag'], y=dfmag2h_1['bz_gsm'],
                        mode='lines',
                        name='Bz'),1,1)
    figsw2h.add_trace(go.Scatter(x=dfmag2h_1['time_tag'], y=dfmag2h_1['bt'],
                        mode='lines',
                        name='Bt'),1,1)
    figsw2h.add_trace(go.Scatter(x=dfp2h_1['time_tag'], y=dfp2h_1['density'],
                        mode='lines',
                        name='Density'),2,1)
    figsw2h.add_trace(go.Scatter(x=dfp2h_1['time_tag'], y=dfp2h_1['speed'],
                        mode='lines',
                        name='Speed'),3,1)
    figsw2h.add_trace(go.Scatter(x=dfp2h_1['time_tag'], y=dfp2h_1['temperature'],
                        mode='lines',
                        name='Temp'),4,1)                   

    figsw2h.update_layout(
        height=900,# width=650,
        xaxis1=dict(showgrid=False, zerolinecolor='grey'),
        yaxis1=dict(showgrid=False, zerolinecolor='grey', range=[-30, 30]),
        xaxis2=dict(showgrid=False),
        yaxis2=dict(showgrid=False, type="log", range=[np.log10(1),np.log10(100)]),
        xaxis3=dict(showgrid=False),
        yaxis3=dict(showgrid=False, range=[200, 800]),
        xaxis4=dict(showgrid=False),
        yaxis4=dict(showgrid=False),
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    return figsw2h

layout = html.Div([
        dbc.Row([
            dbc.Col(html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Aurora Forecast", className='card-title'),
                        html.P("Aurora Oval - Northern Hemisphere", className='card-text'),
                        dcc.Graph(id='auroraoval'),
                        dcc.Interval(
                            id='intauroraoval',
                            interval=60*1000, # in milliseconds
                            n_intervals=0)
                        ], className='card-body')
                ], className='card')
            ],style = CONTENT_STYLE), width=6),
            dbc.Col(html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("All Sky Camera", className='card-title'),
                        html.P("Camera at RASC Calgary", className='card-text'),
                        dcc.Graph(id='rasccamera'),
                        dcc.Interval(
                            id='intrasccamera',
                            interval=60*1000, # in milliseconds
                            n_intervals=0)
                        ], className='card-body')
                ], className='card')
            ],style = CONTENT_STYLE), width=6),
        ]),
        dbc.Row(
            dbc.Col(html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Real-Time Solar Wind", className='card-title'),
                        html.P("Magnetic Plot - 2 hour", className='card-text'),
                        dcc.Graph(id='mag2h-plot', figure = mag_fig(magdf(),plasmadf())),
                        dcc.Interval(
                            id='intmag2h',
                            interval=60*1000, # in milliseconds
                            n_intervals=0)
                        ], className='card-body')
                ], className='card')
            ],style = CONTENT_STYLE)),
        )
])

@app.callback(
    Output('mag2h-plot', 'figure'),
    Input('intmag2h', 'n_intervals'),
    prevent_initial_call=True
)
def mag2hstream(n):
    #today = datetime.datetime.today().date()
    #if magdf()['time_tag'].iloc[0] < today:
        #dash.no_update
    #else:
        return mag_fig(magdf(),plasmadf())

@app.callback(
    Output('auroraoval', 'figure'),
    Input('intauroraoval', 'n_intervals')
)
def auroraovalstream(n):
    srcao = 'https://services.swpc.noaa.gov/images/aurora-forecast-northern-hemisphere.jpg'
    img = io.imread(srcao)
    fig = px.imshow(img)
    fig.update_layout(#height=400, width=400, 
    margin=dict(l=0, r=0, b=0, t=0),
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    coloraxis_showscale=False)
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    return(fig)

@app.callback(
    Output('rasccamera', 'figure'),
    Input('intrasccamera', 'n_intervals')
)
def allskystream(n):
    src = 'https://cam01.sci.ucalgary.ca/AllSkyCam/AllSkyCurrentImage.JPG'
    img = io.imread(src)
    fig = px.imshow(img)
    fig.update_layout(#height=400, width=400, 
    margin=dict(l=0, r=0, b=0, t=0),
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    coloraxis_showscale=False)
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    return(fig)

#if __name__ == '__main__':
#    app.run_server(host="0.0.0.0", port="8050", debug=True)