from dash import html
import dash_bootstrap_components as dbc

CONTENT_STYLE = {
    "margin": "100px 100px",
}

body = html.Div([
        dbc.Row(
            [
            dbc.Col(
                [
                    html.Div([
                    html.Img(src='/assets/architecture.jpg', width = '100%'),
                    ])#, style={"margin": "50px 250px"})
                ]
            )
            ]
        ),     
        dbc.Row([
            dbc.Col(html.Div([
                        html.H4("Tech Stack", style={"padding": "0.5rem"}),
                        html.Ul([
                        html.Li("On-Prem Ubuntu Server", ),
                        html.Li("Kubernetes", ),
                        html.Li("Docker", ),
                        html.Li("NGINX", ),                        
                        html.Li("MongoDB", ),
                        html.Li("Plotly Dash", ),
                        html.Li("Elasticsearch, Fluentd, Kibana (EFK)", ),
                        html.Li("Portainer", ),
                    ])
            ],style = CONTENT_STYLE)),
            dbc.Col(html.Div([
                        html.H4("Data Pipeline", style={"padding": "0.5rem"}),
                        html.Ul([                        
                        html.Li("NOAA and RASC Calgary feed data to the Aurora Dashboard in real-time (refresh rate of 1 min)", ),
                        html.Li("AER provides daily data in text files that go through an ETL process and into a MongoDB database using Python scripts", ),
                        html.Li("MongoDB is used to feed the Explorapp Dashboard directly instead of fully relying on Pandas", ),
                        ])
            ],style = CONTENT_STYLE)),
            dbc.Col(html.Div([
                        html.H4("Future Improvements", style={"padding": "0.5rem"}),
                        html.Ul([
                        html.Li("Refactor code to split into layouts, functions, style, etc. Code begins to get messy when using a broken by app approach", ),
                        html.Li("Automate more the current CI/CD process", ),
                        html.Li("Evaluate moving Python scripts into serverless functions", ),
                        html.Li("Evaluate moving database into cluster", ),
                        html.Li("Evaluate implementing FastAPI", ),
                        html.Li("Evaluate using 3 node cluster to test and enable High Availability", ),
                        html.Li("Fine tune design and add more datasets to existing dashboards", ),                        
                        ])
            ],style = CONTENT_STYLE)),
        ])
])

