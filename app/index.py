from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import About, Architecture, Aurora, OilGas

app.title = 'Jesus Jayaro'
#app._favicon = ("images/logomorado-02-150x150.png")

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

colors = {
    'background': '#FFFFFF',
    'text': '#FFFFFF'
}

style_icon = {
    "padding": "10px 5px",
    "color" : "white",
    'font-size':'40px'
}

style_bottombar = {
    'width': '100%',
    #'height': '100%',
    'position': 'fixed',
    #'vertical-align': 'middle',
    #'text-align': 'center',
    'bottom': 0,
    'z-index': 999,
    #'background': '#FFFFFF'
}

style_topbar = {
    'width': '100%',
    #'height': '100%',
    'position': 'sticky',
    #'vertical-align': 'middle',
    #'text-align': 'center',
    'top': 0,
    'z-index': 999,
    #'background': '#FFFFFF'
}

bottombar = html.Div([dbc.Nav([
        #dbc.NavItem(dbc.NavLink(href="https://ca.linkedin.com/in/jayaro", class_name="far fa-phone", style = style_icon)),
        dbc.NavItem(dbc.NavLink(href="https://github.com/jojayaro", class_name="fab fa-github", style = style_icon)),
        dbc.NavItem(dbc.NavLink(href="https://ca.linkedin.com/in/jayaro", class_name="fab fa-linkedin", style = style_icon)),
        dbc.NavItem(dbc.NavLink(href="https://www.flickr.com/photos/xchus", class_name="fab fa-flickr", style = style_icon)),
        ],
        justified=True,
        ),
        ],style = style_bottombar
        )

body = [
            dbc.Row(
                    dbc.Col(html.Div([
                        html.H1('Hyperautomation Solutions'),
                        html.H3('''
                        Leveraging data and technology to optimize and automate processes that deliver value and ensure success.
                        '''),
                        html.H3(''),
                        dbc.Button("Contact", href = 'https://ca.linkedin.com/in/jayaro', color="primary", className="me-1"),
                    ], style = {'margin':'300px 100px', 'textAlign': 'center', 'line-height': 1.5})
                    )
                ),
            dbc.Row(
                    dbc.Col(html.Div([
                        html.H1('About'),
                        html.H3('This Journey.'),
                        dcc.Link('Learn More', href='/apps/About')
                    ], style = {'margin':'100px 10px', 'textAlign': 'center'})
                    )
                ),
            dbc.Row(
                    dbc.Col([
                        html.Img(src='/assets/about.jpg', width = '100%')
                    ], width=12),
                ),
            dbc.Row(
                    dbc.Col(html.Div([
                        html.H1('Architecture'),
                        html.H3('No. Not that kind of architecture.'),
                        dcc.Link('Learn More', href='/apps/Architecture')
                    ], style = {'margin':'100px 10px', 'textAlign': 'center'})
                    )
                ),
            dbc.Row(
                    dbc.Col([
                        html.Img(src='/assets/architect0.jpg', width = '100%')
                    ], width=12),
                ),
            dbc.Row([
                    dbc.Col([html.Div([
                        html.H1('Aurora Borealis'),
                        html.H3("Data. Photography. How to."),
                        dcc.Link('Learn More', href='/apps/Aurora'),
                    ], style = {'margin':'100px 10px', 'textAlign': 'center'}),
                    ], width = 6),
                    dbc.Col([html.Div([
                        html.H1('Urban Farming'),
                        html.H3('Chili Peppers, Strawberries, and more...'),
                        html.P('Coming Soon'),
                        #dcc.Link('Learn More', href='/apps/Storms'),
                    ], style = {'margin':'100px 10px', 'textAlign': 'center'}),
                    ], width = 6),
            ]),
            dbc.Row([
                    dbc.Col(
                        html.Img(src='/assets/aurora.jpg', width = '100%')
                    , width=6),
                    dbc.Col(
                        html.Img(src='/assets/tomato.jpg', width = '100%')
                    , width=6),
                ]),
            dbc.Row([
                    dbc.Col([html.Div([
                        html.H1('Oil and Gas'),
                        html.H3('Interactive Data!'),
                        dcc.Link('Learn More', href='/apps/OilGas'),
                    ], style = {'margin':'100px 10px', 'textAlign': 'center'}),
                    ], width = 6),
                    dbc.Col([html.Div([
                        html.H1('Traffic Analysis'),
                        html.H3('Taking analysis to the edge.'),
                        html.P('Coming Soon'),
                        #dcc.Link('Learn More', href='/apps/Solutions'),
                    ], style = {'margin':'100px 10px', 'textAlign': 'center'}),
                    ], width = 6),
            ]),
            dbc.Row([
                    dbc.Col(
                        html.Img(src='/assets/rig.jpg', width = '100%')
                    , width=6),
                    dbc.Col(
                        html.Img(src='/assets/Main 3.jpg', width = '100%')
                    , width=6),
            ]),
]

navdropdown = dbc.DropdownMenu(
                    [
                        #dbc.DropdownMenuItem("Solutions", href='/apps/Solutions'),
                        dbc.DropdownMenuItem("Auroras", href='/apps/Auroras'),
                        dbc.DropdownMenuItem("Storms", disabled=True),
                        dbc.DropdownMenuItem("Traffic Analysis", disabled=True),
                        dbc.DropdownMenuItem("Oil and Gas", href='/apps/OilGas'),
                    ],
                    nav=True,
                    in_navbar=True,
                    label='Projects',
                ),

top_logo = dbc.Col(html.Div([
                    html.Img(src='/assets/images/logomorado-02-150x150.png', height='40px'),
                ], style = {'padding':'10px 5px'}),
                    width = 1
                ),

app.layout = dbc.Container([
                html.Div([
                    dbc.Row([
                        dbc.Col(
                            dbc.NavbarSimple(
                                [
                                    dbc.NavItem(dbc.NavLink("Home", href="/")),
                                    dbc.NavItem(dbc.NavLink("About", href="/apps/About")),
                                    dbc.NavItem(dbc.NavLink("Architecture", href="/apps/Architecture")),
                                    dbc.DropdownMenu(
                    [
                        #dbc.DropdownMenuItem("Solutions", href='/apps/Solutions'),
                        dbc.DropdownMenuItem("Auroras", href='/apps/Aurora'),
                        dbc.DropdownMenuItem("Storms", disabled=True),
                        dbc.DropdownMenuItem("Traffic Analysis", disabled=True),
                        dbc.DropdownMenuItem("Oil and Gas", href='/apps/OilGas'),
                    ],
                    nav=True,
                    in_navbar=True,
                    label='Projects',
                ),
                                ],
                                brand="Jesus Jayaro",
                                brand_href="/",
                                color="Primary",
                                #fixed='top',
                                dark=True
                                )
                        ),
                    ])
                    ], style = style_topbar),
                        #,align="center",
                        #className="g-0",
                html.Div([
                dcc.Location(id='url', refresh=False),
                dbc.Row(dbc.Col(html.Div(id='page-content'))),
                ]),
                dbc.Row(dbc.Col(bottombar)),
                ],fluid=True)

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'),
              #prevent_initial_call=True
              )
def display_page(pathname):
    if pathname == '/':
        return body
    elif pathname == '/apps/About':
        return About.body
    elif pathname == '/apps/Aurora':
        return Aurora.body
    elif pathname == '/apps/Architecture':
        return Architecture.body
    elif pathname == '/apps/OilGas':
        return OilGas.body
    else:
        return '404'

if __name__ == '__main__':
    	
    #deployment
	app.run_server()

    #development
    #app.run_server(host="127.0.0.1", port="8050", debug=True)
