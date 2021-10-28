from pickle import TRUE
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from skimage import io
import pymongo
from pandas import json_normalize
import datetime
from app import app

client = pymongo.MongoClient("mongodb://172.17.0.2:27017/")

mapbox_access_token = open("mapbox").read()

st1_substance_list = ['CRUDE BITUMEN', 'CRUDE OIL', 'GAS']

substancedeck = []

##ST1 Map

def st1_map(year,week):
    if year == all and week == all:
        query1 = {'WELL PURPOSE': 'NEW'}
        result = client['AER']['ST1'].find(query1)
        ST1 =  pd.DataFrame(list(result))
    else:
        query1 = {'WELL PURPOSE': 'NEW', 'YEAR': year, 'WEEK': week}
        result = client['AER']['ST1'].find(query1)
        ST1 =  pd.DataFrame(list(result))
    return ST1

##General Group Match Query
def query_group_st1(match,group):
    result = client['AER']['ST1'].aggregate([
            {
                '$match': match
            }, 
            {
                '$group': {
                    '_id': group, 
                    'count': {
                        '$sum': 1
                    }
                }
            },
            {
                '$sort': {
                    'YEAR': -1, 
                    'WEEK': -1, 
                    '_id': 1
                }
            }
                ])
    
    ST1_group_count = json_normalize(result)
    #ST1_group_count = ST1_group_count.sort_values(by=['_id.YEAR', '_id.WEEK'])

    return ST1_group_count

match_dict = {'WELL PURPOSE': 'NEW'}
group_dict = {'YEAR': '$YEAR', 'WEEK': '$WEEK'}

def indicator_fig_value (year,week,substance):
    match_dict = {'WELL PURPOSE': 'NEW', 'YEAR': year, 'WEEK': week, 'SUBSTANCE': substance}
    group_dict = {'YEAR': '$YEAR', 'WEEK': '$WEEK', 'COLUMN': '$SUBSTANCE'}
    filtered_data = query_group_st1(match_dict,group_dict)
    return filtered_data.iloc[0]['count']


#CSS
colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

CONTENT_STYLE = {
    "padding": "1rem 1rem",
}

d = {
    'WATER': 'blue',
    'CRUDE BITUMEN': 'black',
    'CRUDE OIL': 'brown',
    'GAS': 'yellow',
    'NONE': 'orange',
    'WASTE': 'red',
    'BRINE': 'green',
    'LPG': 'purple',
    'COALBED METHANE': 'pink',
    'MISCELLANEOUS': 'cyan',
}

#Date Calculations
today = datetime.datetime.today()
week = today.isocalendar()[1]
current_year = today.isocalendar()[0]

try:
    indicator_fig_value(current_year, week,'GAS') & indicator_fig_value(current_year, week,'CRUDE BITUMEN') & indicator_fig_value(current_year, week,'CRUDE OIL')
    current_week = today.isocalendar()[1]
except:
    current_week = today.isocalendar()[1] - 1
    
#Graphs
##Main Graph
ST1_group_count = query_group_st1(match_dict,group_dict)

weeklydataperyear = px.bar(ST1_group_count, x = ST1_group_count['_id.WEEK'], 
                y = ST1_group_count['count'], 
                color = ST1_group_count['_id.YEAR'].astype(str),
                hover_data = ['_id.YEAR', '_id.WEEK']
            )

weeklydataperyear.update_layout(xaxis=dict(title='Week', showgrid=False, zerolinecolor='grey'),
            yaxis=dict(title='Count',showgrid=False),
            legend=dict(title='Year'),
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text']
            )

##Functions

def st1map_fig(df):
    
    #midpoint = (np.average(df['Lat']), np.average(df['Long']))
    
    dfmap = go.Figure()

    sub_list = df['SUBSTANCE'].unique()
    for sub in sub_list:
        dfmap.add_trace(go.Scattermapbox(
            lat=df[df['SUBSTANCE'] == sub]['Lat'],
            lon=df[df['SUBSTANCE'] == sub]['Long'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=10,
                color= d[sub]
            ),
            text=df[df['SUBSTANCE'] == sub]['LICENSEE'],
            name=sub,
            customdata=df[df['SUBSTANCE'] == sub]['LICENCE NUMBER'],
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
            center=go.layout.mapbox.Center(
                lat=53.9333,
                lon=-116.5765
            ),
            pitch=0,
            zoom=4,
            style='dark'
        )
    )
    return dfmap

def substance_count(substance):
    match_dict = {'WELL PURPOSE': 'NEW', 'SUBSTANCE': substance}
    group_dict = {'YEAR': '$YEAR', 'WEEK': '$WEEK', 'COLUMN': '$SUBSTANCE'}
    filtered_data = query_group_st1(match_dict,group_dict)
    return filtered_data.iloc[0]['count']

def indicator_fig (substance, value):
    indicator = go.Figure(go.Indicator(
                    title = {'text': substance, 'font': {'size': 18}},
                    mode = "number",
                    number = {"font":{"size":20}},
                    value = value,
                ))
    indicator.update_layout(height = 100,
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)
    return indicator

for substance in st1_substance_list:
    substancedeck.append(dbc.Card([
            dbc.CardBody([
                dcc.Graph(id = substance, figure = indicator_fig(substance, indicator_fig_value(current_year, current_week, substance)))                             
            ])
        ])
    )

def sunburst_fig(year,week):
    match_dict = {'WELL PURPOSE': 'NEW', 'YEAR': year, 'WEEK': week}
    group_dict = {'YEAR': '$YEAR', 'WEEK': '$WEEK', 'DRILLING OPERATION': '$DRILLING OPERATION', 'LICENSEE': '$LICENSEE'}
    SUNNY = query_group_st1(match_dict,group_dict)
    fig =px.sunburst(SUNNY, path=['_id.DRILLING OPERATION', '_id.LICENSEE'], values='count')
    fig.update_layout(        
            height = 800,
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text']
    )
    return fig


#Layout
layout = html.Div([
        dbc.Row([
            dbc.Col(html.Div(
                [
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Alberta Licence and Spud Data", className='card-title'),
                            html.P("This project takes licence and spud data provided by the Alberta Energy Regulator (AER) daily in text format. This data is then parsed and transformed using a python script and loaded into a MongoDB database. MongoDB feeds the dashboard directly without fully relying on Pandas", className='card-text'),
                        ])
                    ]),
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Sample Text File", className='card-title'),
                            dbc.CardImg(src='/assets/samplefile.png')
                        ])
                    ])
                ],style = CONTENT_STYLE),
            )
        ]),
        dbc.Row([
            dbc.Col(html.Div(
                    substancedeck,
                    id = 'substancedeck',
            ), style = CONTENT_STYLE)    
        ]),
        dbc.Row(
            dbc.Col(html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("New Licences issued per week", className='card-title'),
                        html.P("Click on an specific week/year to update labels and graphs (showing current week by default)", className='card-text'),
                        html.P("Clicking on the legend allows you to remove or add years to the graph", className='card-text'),
                        html.P("(Source: AER)", className='card-text'),
                       dcc.Graph(id = 'weeklydataperyear', figure = weeklydataperyear)
                        ])
                ])
            ],style = CONTENT_STYLE)),
        ),
        dbc.Row(
            dbc.Col(html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Approximate locations of wells", className='card-title'),
                        html.P("Based on ST1 data", className='card-text'),
                        html.P("(Source: AER)", className='card-text'),
                        dcc.Graph(id = 'st1map', figure = st1map_fig(st1_map(current_year,current_week)))
                        ])
                ])
            ],style = CONTENT_STYLE)),
        ),
        dbc.Row([
            dbc.Col(html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Licensee(s) by Type of Operation", className='card-title'),
                        html.P("Based on current week or clicked data", className='card-text'),
                        html.P("Press on the type of operation to drill down", className='card-text'),
                        html.P("(Source: AER)", className='card-text'),
                        dcc.Graph(id = 'licensees', figure = sunburst_fig(current_year,current_week))
                        ])
                ])
            ],style = CONTENT_STYLE)),
        ]),
        dbc.Modal(
            [
                dbc.ModalHeader("Header"),
                dbc.ModalBody(id = 'modal-body'),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close", className="ml-auto", n_clicks=0
                    )
                ),
            ],
            id="modal",
            is_open=False,
        ),
])

#Callbacks

@app.callback(
    Output('CRUDE BITUMEN', 'figure'),
    Output('CRUDE OIL', 'figure'),
    Output('GAS', 'figure'),
    Output('st1map', 'figure'),
    Output('licensees', 'figure'),
    Input('weeklydataperyear', 'clickData'),
    prevent_initial_call=True
)
def filtered_weekly_yearly(clkd_data):
    if clkd_data is None:
        dash.no_update
    else:
        #print(f'clickData: {clkd_data}')
        week = clkd_data['points'][0]['x']
        year = clkd_data['points'][0]['customdata'][0]

        CRUDE_BITUMEN = indicator_fig('CRUDE BITUMEN', indicator_fig_value (year,week,'CRUDE BITUMEN'))
        CRUDE_OIL = indicator_fig('CRUDE OIL', indicator_fig_value (year,week,'CRUDE OIL'))
        GAS = indicator_fig('GAS', indicator_fig_value (year,week,'GAS'))
        st1map = st1map_fig(st1_map(year,week))
        lic_fig = sunburst_fig(year,week)
        return CRUDE_BITUMEN, CRUDE_OIL, GAS, st1map, lic_fig
 
