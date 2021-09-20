from dash import html
import dash_bootstrap_components as dbc

CONTENT_STYLE = {
    "padding": "1rem 1rem",
}

layout = html.Div([
        dbc.Row(
            dbc.Col(html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H2("Architecture", className='card-title'),
                        ], className='card-body')
                ], className='card')
            ],style = CONTENT_STYLE)),
        ),
        dbc.Row(
            dbc.Col(html.Div([
                dbc.Card([
                    dbc.CardBody([
                            dbc.CardImg(src='/assets/architecture.jpg'),
                        ], className='card-body')
                ], className='card')
            ],style = CONTENT_STYLE)),
        ),        
        dbc.Row(
            dbc.Col(html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Server Elements:", className='card-text'),
                        html.Li("Local Ubuntu Server", className='card-text'),
                        html.Li("MongoDB database is runs in docker", className='card-text'),
                        html.Li("Kubernetes is used to orchestrate the webapp", className='card-text'),
                        html.Li("NGINX reverse proxy is used to manage access to the webapp", className='card-text'),
                        html.Li("Portainer is used to manage containers in Docker and Kubernetes", className='card-text'),
                    ]),
                ], className='card')
            ],style = CONTENT_STYLE)),
        ),
        dbc.Row(
            dbc.Col(html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Data Pipeline:", className='card-text'),
                        html.Li("NOAA and RASC Calgary feed data to the Aurora Dashboard in real-time", className='card-text'),
                        html.Li("AER provides daily data in text files that go through an ETL process into a MongoDB database using python scripts", className='card-text'),
                        html.Li("MongoDB is used to feed the Explorapp Dashboard directly instead of fully relying in Pandas", className='card-text'),
                        html.P(" ", className='card-text'),
                        ], className='card-body')
                ], className='card')
            ],style = CONTENT_STYLE)),
        )
])

