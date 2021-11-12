import pandas as pd
import plotly.graph_objects as go
from dash import html, dcc
import dash_bootstrap_components as dbc

profile_df = pd.read_csv("apps/assets/profile.csv")
profile_table = profile_df.drop(columns=['City','Latitude', 'Longitude', 'State/Province', 'Description'])
#sort profile_table by column End
profile_table = profile_table.sort_values(by=['End'], ascending=False)

d = {
    'Life': 'green',
    'Work': 'red',
    'Education': 'blue',
}

mapbox_access_token = open("mapbox").read()

colors = {
    'background': '#060606',
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
            customdata=df[df['Activity'] == sub]['Country'],
        ))

    dfmap.update_layout(
        height = 800,
        #width = 800,
        hovermode='closest',
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
        legend=dict(
        orientation="h",
        xanchor="center",
        x=0.5
        ),
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            pitch=0,
            center=go.layout.mapbox.Center(
                lat=22.5,
                lon=-34.5
            ),            
            zoom=0.8,
            style='dark'
        )
    )
    return dfmap

body = html.Div([
dbc.Row([
    dbc.Col(
        html.Div([
            html.Img(src='/assets/YYC.jpg', width = '100%'),
        ])
    )
]),
        dbc.Row([
            dbc.Col(html.Div([
                        dcc.Markdown('''
Energy, the thing that has allowed us to evolve, and the same thing that holds us back. It is a precious resource which we rely on, and something that can be taken away as well. We are inefficient at transforming it, or perhaps primitive, and there is a lot of wasted energy. Efficiency is our end goal, minimize the waste. How to achieve it?
  
Energy or effort is used or exerted everywhere, there is always room to make anything more efficient. It is studied and applied in many different ways.
  
One area that is vital to our existence is Agriculture. Here we are very inefficient in many ways such as distance traveled from farm to table or the amount of excess fertilizer used. One way to mitigate this is in-situ farming, producing as much as possible locally. This can also generate jobs locally that are sustainable over time. This is also now possible even at high latitude locations due to the availability of LEDs, which currently is also the most efficient lighting solution all around.
  
Another area is Lean, in short you want to improve to achieve excellence and deliver value. To improve you must measure, and to be able to measure you need data. Advances in technology have enabled us to collect data about everything every second. The opportunity to excel as an individual, community, organization, or a nation is within our reach.
  
Space Weather is something that is not widely discussed. Just like weather is monitored on Earth, there are instruments in space which provide data on solar physics among other things. This data can be useful to predict the occurrence of aurora borealis, with the caveat that you have only about thirty minutes to an hour of head start. Data is open and available to the public through NOAA. How is this related to energy? Some solar events have caused damage to energy infrastructure in the past, and a greater event could set us back technologically.
  
Last, idling wastes energy, so traffic analysis is essential in improving energy use. Computer vision has enabled us to automate this highly labor intensive and manual data collection task with high accuracy. Alongside other technologies such as Cloud Native Edge Computing, Autonomous Drones, 5G, and Reinforcement Learning the opportunity to improve traffic regardless of means of transportation needs to be exploited. These technologies also open many doors to improve many aspects of our communities.
                        '''
                        ),
            ], style = {'margin-top':'30px', 'padding':'100px 30px'}), width = 7),
            dbc.Col(html.Div([
                dcc.Graph(id = 'profile_map', figure = map_fig(profile_df), config={'displayModeBar': False})
            ]), width = 5),
        ]),
        dbc.Row([
            dbc.Col(html.Div([
                        html.H4("Values", style={"padding": "0.5rem"}),
                        html.Ul([
                        html.Li("Exceed customer expectations"),
                        html.Li("Deliver value in every service and product"),
                        html.Li("Create great experiences"),
                ])
            ]),width = 4),
            dbc.Col(html.Div([
                        html.H4("Hobbies", style={"padding": "0.5rem"}),
                        html.Ul([
                        html.Li("Photography"),
                        html.Li("Aurora and Storm Chasing"),
                        html.Li("Mountain Biking"),
                        html.Li("Urban Farming"),
                        html.Li("Geopolitics"),                        
                        html.Li("Technology"),
                ])
            ]),width = 4),
            dbc.Col(html.Div([
                        html.H4("Tech Stack", style={"padding": "0.5rem"}),
                        html.Ul([
                        html.Li("Azure, Dynamics, Power Platform"),
                        html.Li("Plotly Dash"),
                        html.Li("MongoDB"),
                        html.Li("Docker"),
                        html.Li("Kubernetes"),
                        html.Li("Portainer"),
                        html.Li("Elasticsearch, Fluentd, Kibana (EFK)"),
                ])
            ]),width = 4),
        ],style = {'margin':'100px 100px'}),
        dbc.Row(
            dbc.Col(html.Div([
                        html.H3("Experience"),
            ],style = {'margin':'70px 10px', 'textAlign': 'center', 'line-height': 1.5})),
        ),
        dbc.Row(
            dbc.Col(html.Div([
                            dbc.Table.from_dataframe(profile_table, striped=True, bordered=True, hover=True, id = 'profile_table'),
            ],style = {'padding':'50px 30px', 'textAlign': 'center'})),
        ),
        ])