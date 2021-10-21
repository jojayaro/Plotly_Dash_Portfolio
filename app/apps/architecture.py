from dash import html
import dash_bootstrap_components as dbc

CONTENT_STYLE = {
    "padding": "1rem 1rem",
}

layout = html.Div([
        dbc.Row(
            [
            dbc.Col(
                [
                    html.H1("Architecture", style={"padding": "1.5rem", 'textAlign': 'center'}),
                ]
            )
            ]
        ),
        dbc.Row(
            [
            dbc.Col(
                [
                    html.Div([
                    html.Img(src='/assets/architecture.jpg', width = '100%'),
                    ], style={"padding": "1rem 1rem"})
                ]
            )
            ]
        ),     
        dbc.Row(
            dbc.Col(html.Div([
                        html.H4("Tech Stack", style={"padding": "0.5rem"}),
                        html.Ul([
                        html.Li("Local Ubuntu Server", className='card-text'),
                        html.Li("Kubernetes", className='card-text'),
                        html.Li("Docker", className='card-text'),
                        html.Li("NGINX", className='card-text'),                        
                        html.Li("MongoDB", className='card-text'),
                        html.Li("Plotly Dash", className='card-text'),
                        html.Li("Elasticsearch, Fluentd, Kibana (EFK)", className='card-text'),
                        html.Li("Portainer", className='card-text'),
                        html.Li("ArgoCD"),
                ])
            ],style = CONTENT_STYLE)),
        ),
        dbc.Row(
            dbc.Col(html.Div([
                        html.H4("Data Pipeline", style={"padding": "0.5rem"}),
                        html.Ul([                        
                        html.Li("NOAA and RASC Calgary feed data to the Aurora Dashboard in real-time (refresh rate of 1 min)", className='card-text'),
                        html.Li("AER provides daily data in text files that go through an ETL process and into a MongoDB database using Python scripts", className='card-text'),
                        html.Li("MongoDB is used to feed the Explorapp Dashboard directly instead of fully relying on Pandas", className='card-text'),
                        ])
            ],style = CONTENT_STYLE)),
        ),
        dbc.Row(
            dbc.Col(html.Div([
                        html.H4("Future Improvements", style={"padding": "0.5rem"}),
                        html.Ul([
                        html.Li("Refactor code to split into layouts, functions, style, etc. Code begins to get messy when using a broken by app approach", className='card-text'),
                        html.Li("Automate more the current CI/CD process", className='card-text'),
                        html.Li("Evaluate moving Python scripts into serverless functions", className='card-text'),
                        html.Li("Evaluate moving database into cluster", className='card-text'),
                        html.Li("Evaluate implementing FastAPI", className='card-text'),
                        html.Li("Evaluate using 3 node cluster to test and enable High Availability", className='card-text'),
                        html.Li("Fine tune design and add more datasets to existing dashboards", className='card-text'),                        
                        ])
            ],style = CONTENT_STYLE)),
        )
])

