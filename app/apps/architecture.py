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
                        html.Li("MongoDB database runs in Docker", className='card-text'),
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
                        html.Li("NOAA and RASC Calgary feed data to the Aurora Dashboard in real-time (refresh rate of 1 min)", className='card-text'),
                        html.Li("AER provides daily data in text files that go through an ETL process and into a MongoDB database using Python scripts", className='card-text'),
                        html.Li("MongoDB is used to feed the Explorapp Dashboard directly instead of fully relying on Pandas", className='card-text'),
                        html.P(" ", className='card-text'),
                        ], className='card-body')
                ], className='card')
            ],style = CONTENT_STYLE)),
        ),
        dbc.Row(
            dbc.Col(html.Div([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Improvements:", className='card-text'),
                        html.Li("Refactor code to split into layouts, functions, style, etc. Code begins to get messy when using a broken by app approach", className='card-text'),
                        html.Li("Create views at the Database level to improve queries/code", className='card-text'),
                        html.Li("Automate more current CI/CD process", className='card-text'),
                        html.Li("Evaluate using Airflow for pipelines", className='card-text'),
                        html.Li("Evaluate moving Python scripts into serverless functions", className='card-text'),
                        html.Li("Evaluate moving database into cluster and implementing Longhorn or equivalent", className='card-text'),
                        html.Li("Evaluate implementing FastAPI", className='card-text'),
                        html.Li("Evaluate using a pico cluster to test and enable High Availability", className='card-text'),
                        html.Li("Fine tune design and add more datasets to existing dashboards", className='card-text'),                        
                        html.P(" ", className='card-text'),
                        ], className='card-body')
                ], className='card')
            ],style = CONTENT_STYLE)),
        )
])

