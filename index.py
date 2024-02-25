from dash import Dash, html, dcc, Input, Output, State

# Assuming you've imported your app and page layouts from the respective modules
from app import app
import apps.home as home
import apps.chatbot as chatbot
import apps.recycling_bins as recycling_bins
import apps.recyclable_checker as recyclable_checker

# Define the layout for the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Add this line

    html.Div([
        html.Button('☰', id='menu-button', n_clicks=0, className='menu-button'),
        html.Div([
            html.Div([
                html.Img(src='assets/home.png', className='icon'),
                dcc.Link('Home', href='/', className='sidebar-link'),
            ]),
            html.Div([
                html.Img(src='assets/chatbot.png', className='icon'),
                dcc.Link('Chatbot', href='/chatbot', className='sidebar-link'),
            ]),
            html.Div([
                html.Img(src='assets/bin.png', className='icon'),
                dcc.Link('Recycling Bins', href='/recycling-bins', className='sidebar-link'),
            ]),
            html.Div([
                html.Img(src='assets/recycle.png', className='icon'),
                dcc.Link('Recyclable Checker', href='/recyclable-checker', className='sidebar-link'),
            ]),
            html.Div([
                html.Img(src='assets/profile-user.png', className='icon'),
                dcc.Link('Profile User', href='/profile user', className='sidebar-link'),
            ])

        ], className='sidebar', id='sidebar'),
    ]),
    html.Div(id='page-content', className='content'),
], className='container')

# Define the callback for the sidebar toggle
@app.callback(
    Output('sidebar', 'style'),
    [Input('menu-button', 'n_clicks')],
    [State('sidebar', 'style')]
)
def toggle_sidebar(n_clicks, sidebar_style):
    if n_clicks and n_clicks % 2 == 1:
        # Sidebar is hidden
        return {'display': 'none'}
    else:
        # Sidebar is visible
        return {'display': 'block'}

# Define the callback for dynamic page loading
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/chatbot':
        return chatbot.layout
    elif pathname == '/recycling-bins':
        return recycling_bins.layout
    elif pathname == '/recyclable-checker':
        return recyclable_checker.layout
    else:  # Default is home page
        return home.layout

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
