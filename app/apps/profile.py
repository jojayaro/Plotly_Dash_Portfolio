from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
from app import app
import dash



CONTENT_STYLE = {
    "padding": "1rem 1rem",
}

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
        dbc.Row(
            dbc.Col(html.Div([
                dbc.Card([
                    dbc.CardBody([
                            dbc.Table.from_dataframe(profile_table, striped=True, bordered=True, hover=True, id = 'profile_table'),
                        ], className='card-body')
                ], className='card')
            ],style = CONTENT_STYLE)),
        ),
])

#callback to update the table based on the marker clicked
@app.callback(
    Output('profile_table', 'data'),
    [Input('profile_map', 'clickData')]
    )
#function to update the table based on the marker clicked
def update_table(clickData):
    if clickData is None:
        dash.no_update
    else:
        print(f'clickData: {clickData}')
        country = clickData['points'][0]['customdata'][0]
        #filter the table based on the country
        filtered_df = profile_df[profile_df['Country'] == country]
        return filtered_df.to_dict('records')





