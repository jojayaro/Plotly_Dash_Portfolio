import dash
import dash_bootstrap_components as dbc

#Deployment
from flask import Flask
server = Flask(__name__)
app = dash.Dash(server=server, external_stylesheets=[dbc.themes.CYBORG, dbc.icons.FONT_AWESOME])

#Development
#app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.CYBORG, dbc.icons.FONT_AWESOME])
#server = app.server