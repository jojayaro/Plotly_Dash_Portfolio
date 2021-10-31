from dash import dcc, html, Input, Output
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

colors = {
    'background': '#060606',
    'text': '#FFFFFF'
}

CONTENT_STYLE = {
    "padding": "10px 10px",
}

#Functions
def auroraoval():
    src1 = 'https://services.swpc.noaa.gov/images/aurora-forecast-northern-hemisphere.jpg'
    img = io.imread(src1)
    fig1 = px.imshow(img)
    fig1.update_layout(#height=400, width=400, 
    margin=dict(l=0, r=0, b=0, t=0),
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    coloraxis_showscale=False)
    fig1.update_xaxes(showticklabels=False, visible = False)
    fig1.update_yaxes(showticklabels=False, visible = False)
    return fig1

def rasccalgary():
    src2 = 'https://cam01.sci.ucalgary.ca/AllSkyCam/AllSkyCurrentImage.JPG'
    img = io.imread(src2)
    fig2 = px.imshow(img)
    fig2.update_layout(#height=400#, width=400, 
    margin=dict(l=0, r=0, b=0, t=0),
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    coloraxis_showscale=False)
    fig2.update_xaxes(showticklabels=False, visible = False)
    fig2.update_yaxes(showticklabels=False, visible = False)
    return fig2

def suvi131():
    src3 = 'https://services.swpc.noaa.gov/images/animations/suvi/primary/131/latest.png'
    img = io.imread(src3)
    fig3 = px.imshow(img)
    fig3.update_layout(#height=400#, width=400,
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False), 
    margin=dict(l=0, r=0, b=0, t=0, pad = 0),
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    coloraxis_showscale=False)
    fig3.update_xaxes(showticklabels=False, visible = False)
    fig3.update_yaxes(showticklabels=False, visible = False)
    return fig3

def geocolor():
    src4 = 'https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/can/GEOCOLOR/2250x1125.jpg'
    img = io.imread(src4)
    fig4 = px.imshow(img)
    fig4.update_layout(height=1125,# width=400, 
    margin=dict(l=0, r=0, b=0, t=0),
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    coloraxis_showscale=False)
    fig4.update_xaxes(showticklabels=False, visible = False)
    fig4.update_yaxes(showticklabels=False, visible = False)
    return fig4

def xray():
    urlxray = 'https://services.swpc.noaa.gov/json/goes/primary/xrays-3-day.json'
    responsexray = urllib.request.urlopen(urlxray)
    dataxray = json.loads(responsexray.read().decode())
    dfxray = pd.DataFrame(dataxray)
    dfxray_1 = dfxray[['time_tag','flux','observed_flux']]
    dfxray_1['time_tag'] = pd.to_datetime(dfxray_1['time_tag'])
    dfxray_1['flux'] = dfxray_1['flux'].astype(float)
    dfxray_1['observed_flux'] = dfxray_1['observed_flux'].astype(float)
    return dfxray_1

def figxray(dfxray_1):
    figxray = make_subplots(rows=1, cols=1)
    figxray.add_trace(go.Scatter(x=dfxray_1['time_tag'], y=dfxray_1['flux'],
                        mode='lines',
                        name='Flux'),1,1)
    figxray.add_trace(go.Scatter(x=dfxray_1['time_tag'], y=dfxray_1['observed_flux'],
                        mode='lines',
                        name='Observed Flux'),1,1)                     

    figxray.update_layout(
        height=800,# width=650,
        xaxis1=dict(showgrid=False),# zerolinecolor='grey'),
        yaxis1=dict(showgrid=False),# zerolinecolor='grey'),#, range=[-30, 30]),
        xaxis2=dict(showgrid=False),
        yaxis2=dict(showgrid=False),# type="log", range=[np.log10(1),np.log10(100)]),
        xaxis3=dict(showgrid=False),
        yaxis3=dict(showgrid=False),# range=[200, 800]),
        xaxis4=dict(showgrid=False),
        yaxis4=dict(showgrid=False),
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    return figxray

def epam():
    urlepam = 'https://services.swpc.noaa.gov/json/ace/epam/ace_epam_5m.json'
    responseepam = urllib.request.urlopen(urlepam)
    dataepam = json.loads(responseepam.read().decode())
    dfepam = pd.DataFrame(dataepam)
    dfepam_1 = dfepam[['time_tag','de1','de4','p1', 'p3','p5','fp6p','p7']]
    dfepam_1['time_tag'] = pd.to_datetime(dfepam_1['time_tag'])
    dfepam_1['de1'] = dfepam_1['de1'].astype(float)
    dfepam_1['de4'] = dfepam_1['de4'].astype(float)
    dfepam_1['p1'] = dfepam_1['p1'].astype(float)
    dfepam_1['p3'] = dfepam_1['p3'].astype(float)
    dfepam_1['p5'] = dfepam_1['p5'].astype(float)
    dfepam_1['fp6p'] = dfepam_1['fp6p'].astype(float)
    dfepam_1['p7'] = dfepam_1['p7'].astype(float)
    return dfepam_1

def figepam(dfepam_1):
    figepam = make_subplots(rows=3, cols=1)
    figepam.add_trace(go.Scatter(x=dfepam_1['time_tag'], y=dfepam_1['de1'],
                        mode='lines',
                        name='Electrons 175-315'),1,1)
    figepam.add_trace(go.Scatter(x=dfepam_1['time_tag'], y=dfepam_1['de4'],
                        mode='lines',
                        name='Electrons 38-53'),1,1)
    figepam.add_trace(go.Scatter(x=dfepam_1['time_tag'], y=dfepam_1['p1'],
                        mode='lines',
                        name='Protons 47-68'),2,1)
    figepam.add_trace(go.Scatter(x=dfepam_1['time_tag'], y=dfepam_1['p3'],
                        mode='lines',
                        name='Protons 115-195'),3,1)
    figepam.add_trace(go.Scatter(x=dfepam_1['time_tag'], y=dfepam_1['p5'],
                        mode='lines',
                        name='Protons 310-580'),3,1)
    figepam.add_trace(go.Scatter(x=dfepam_1['time_tag'], y=dfepam_1['fp6p'],
                        mode='lines',
                        name='Protons 795-1193'),3,1)
    figepam.add_trace(go.Scatter(x=dfepam_1['time_tag'], y=dfepam_1['p7'],
                        mode='lines',
                        name='Protons 1060-1900'),3,1)                        

    figepam.update_layout(
        height=800,# width=650,
        xaxis1=dict(showgrid=False),# zerolinecolor='grey'),
        yaxis1=dict(showgrid=False),# zerolinecolor='grey', range=[-30, 30]),
        xaxis2=dict(showgrid=False),
        yaxis2=dict(showgrid=False),# type="log", range=[np.log10(1),np.log10(100)]),
        xaxis3=dict(showgrid=False),
        yaxis3=dict(showgrid=False),# range=[200, 800]),
        xaxis4=dict(showgrid=False),
        yaxis4=dict(showgrid=False),
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    return figepam

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
        height=800,# width=650,
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

body = [

dbc.Row([
    dbc.Col(
        html.Div([
            html.Img(src='/assets/auroracar2.jpg', width = '100%'),
        ])
    )
]),
dbc.Row([
    dbc.Col(
        html.Div([
                dcc.Graph(id='suvi131', figure=suvi131()),
                html.P("GOES-16 SUVI Composite 131 Angstroms (Source: NOAA SWPC)"),
                dcc.Interval(
                    id='intimages',
                    interval=60*1000, # in milliseconds
                    n_intervals=0)
        ], style={"margin": "200px 10px", 'textAlign': 'center'}), width = 5),
    dbc.Col(
        html.Div([
            dcc.Graph(id='xray', figure = figxray(xray())),
            html.P("GOES X-Ray Flux (Source: NOAA SWPC)"),
            dcc.Interval(
                id='intgraphs',
                interval=60*1000, # in milliseconds
                n_intervals=0)
        ], style={"margin": "0px 10px", 'textAlign': 'center'}), width=7),
]),
dbc.Row([
    dbc.Col(
        html.Div([
            dcc.Graph(id='epam', figure = figepam(epam())),
            html.P("Electron Proton Alpha Monitor (Source: NOAA SWPC)"),
        ], style={"margin": "0px 10px", 'textAlign': 'center'}), width=7),
    dbc.Col(
        html.Div([
                dcc.Graph(id='auroraoval', figure = auroraoval()),
                html.P("Aurora Oval - Northern Hemisphere (Source: NOAA SWPC)"),
        ], style={"margin": "200px 10px", 'textAlign': 'center'}), width=5),
]),
dbc.Row([
    dbc.Col(
        html.Div([
                dcc.Graph(id='rasccamera', figure = rasccalgary()),
                html.P("Live stream feed from Calgary (Source: RASC Calgary)"),
        ], style={"margin": "200px 10px", 'textAlign': 'center'}), width = 5),
    dbc.Col(
        html.Div([
            dcc.Graph(id='mag2h-plot', figure = mag_fig(magdf(),plasmadf())),
                        html.P("Magnetic and Plasma Plot - 2 hour (Source: NOAA SWPC)"),
            html.P("Note: Double click on data to auto resize the axes"),
            dcc.Interval(
                id='intgraphs',
                interval=60*1000, # in milliseconds
                n_intervals=0)
        ], style={"margin": "0px 10px", 'textAlign': 'center'}), width=7),
]),
dbc.Row(
    dbc.Col(
        html.Div([
                dcc.Graph(id='weather', figure = geocolor()),
                html.P("GOES-16 GeoColor (Source: NOAA)"),
                dcc.Interval(
                    id='intgeocolor',
                    interval=60*10000, # in milliseconds
                    n_intervals=0)
        ], style={"margin": "0px 10px", 'textAlign': 'center', 'width':'100%'}), width=12),
)
]

@app.callback(
    Output('xray', 'figure'),
    Output('epam', 'figure'),
    Output('mag2h-plot', 'figure'),
    Input('intgraphs', 'n_intervals'),
    #prevent_initial_call=True
)
def mag2hstream(n):
    return figxray(xray()), figepam(epam()), mag_fig(magdf(),plasmadf()) 

@app.callback(
    Output('auroraoval', 'figure'),
    Output('rasccamera', 'figure'),
    Output('suvi131', 'figure'),
    Input('intimages', 'n_intervals')
)
def imagescb(n):
    return auroraoval(), rasccalgary(), suvi131()

@app.callback(
    Output('weather', 'figure'),
    Input('intgeocolor', 'n_intervals')
)
def imagescb(n):
    return geocolor()
