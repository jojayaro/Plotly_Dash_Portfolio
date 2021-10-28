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
                        html.P("Being a child of two university professors I had the opportunity to play with computers from an early age. This sparked my curiosity into how computer systems work and their endless applications. I listened to university computer science courses, and even participated in computer building and maintenance workshops. This enabled me to deep dive into computer science and fall in love with it as a kid.", style={"padding": "0.5rem"}),
                        html.P('All of this plus my passion for energy, led me to pursue my studies in Mechanical Engineering and focus in Instrumentation and Measurements and Control Systems. During my college years I worked for a Hurricane Research project where we deployed real-time data acquisition and monitoring systems during the 2005 and 2006 Hurricane Season. Field deployments included major Hurricanes Dennis, Katrina, and Wilma.', style={"padding": "0.5rem"}),
                        html.P('After graduation, I worked for different oil and gas services companies in Operations, and Product and Service Quality. Focus was on Automation, Reliability, Root Cause Analysis and Lean Six Sigma. I had to perform data analysis, design, develop, and deploy real-time reporting and collaboration solutions to be able to provide the best strategies to eliminate non-conformities and non-productive time, which in turn allowed me to minimize red money and maximize customer success and promote sales growth while creating a great experience for all customers. ', style={"padding": "0.5rem"}),
                        html.P('On the research side, I have always made it my priority to perform market research and intelligence to be up to date with latest trends and technologies in order to differentiate services and products offered and be at the cutting edge, and to better gauge where the market is heading.', style={"padding": "0.5rem"}),
            ], style = {'margin-top':'30px', 'padding':'100px 30px'}), width = 7),
            dbc.Col(html.Div([
                dcc.Graph(id = 'profile_map', figure = map_fig(profile_df))
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