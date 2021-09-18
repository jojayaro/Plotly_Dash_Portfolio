import dash
import dash_bootstrap_components as dbc
import pandas as pd
from flask import Flask

server = Flask(__name__)

app = dash.Dash(server=server, external_stylesheets=[dbc.themes.DARKLY])
app.title = 'Jesus Jayaro'

app.index_string = """<!DOCTYPE html>
<html>
    <head>
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-LCYV5QDN4X"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-LCYV5QDN4X');
        </script>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>"""

from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import darkauroradash, explorapp, architecture

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

app.layout = dbc.Container([
    dbc.Row(dbc.Col(
    dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Profile", href="/apps/profile")),
        dbc.NavItem(dbc.NavLink("Architecture", href="/apps/architecture")),
        dbc.DropdownMenu(
            label='Projects',
            children=[
                dbc.DropdownMenuItem("Explorapp", href='/apps/explorapp'),
                dbc.DropdownMenuItem("Dark Aurora Dashboard", href="/apps/darkauroradash"),
                #dbc.DropdownMenuItem("Naked Eye Aurora", href='/'),
            ],
            nav=True,
            in_navbar=True,
        ),
        dbc.NavItem(dbc.NavLink("LinkedIn", href="https://ca.linkedin.com/in/jayaro"))
    ],
    brand="Jesus Jayaro",
    brand_href="/",
    color="primary",
    dark=True
    ))),
    html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
    ]),

    ],)#fluid=True)

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return     dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    dbc.CardImg(src='/assets/Headshot_Main.jpg'),
                                    dcc.Interval(
                                        id='intmag2h',
                                        interval=60*1000, # in milliseconds
                                        n_intervals=0)
                                    ])
                                ])
                            ], width=12),
                        ]),
    elif pathname == '/apps/darkauroradash':
        return darkauroradash.layout
    elif pathname == '/apps/explorapp':
        return explorapp.layout
    elif pathname == '/apps/architecture':
        return architecture.layout
    #elif pathname == '/apps/profile':
        #return profile.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server()
