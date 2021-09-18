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
                        html.H4("Server Elements:", className='card-text'),
                        html.Li("Server is local", className='card-text'),
                        html.Li("Ubuntu Server is the operating system", className='card-text'),
                        html.Li("Docker is used to host the MongoDB database", className='card-text'),
                        html.Li("Kubernetes is used to orchestrate the webapp", className='card-text'),
                        html.Li("NGINX reverse proxy is used to manage access to the webapp", className='card-text'),
                        html.Li("Portainer is used to manage containers in Docker and Kubernetes", className='card-text'),
                        html.H4("Data Pipeline:", className='card-text'),
                        html.Li("NOAA and RASC Calgary feed data to the Aurora Dashboard in real-time", className='card-text'),
                        html.Li("AER provides daily data in text files that are ETLd into a MongoDB database using python scripts", className='card-text'),
                        html.Li("MongoDB then feeds the Alberta Exploration Dashboard", className='card-text'),
                        html.P(" ", className='card-text'),
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
        )
])

