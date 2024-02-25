from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from app import app  # Assuming you have imported 'app' from app.py

# Define the layout for the recyclable checker page
layout = html.Div([
    html.H2("Recyclable Item Checker", className="checker-header"),
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            html.I(className="fa fa-file-upload fa-3x", style={'paddingRight': '10px'}),  # Add a file upload icon
            'Drag and Drop or ',
            html.A('Select an Image')
        ]),
        style={
            'width': '100%',
            'height': '100px',  # Increase the height
            'lineHeight': '100px',  # Increase the line height to vertically center the contents
            'borderWidth': '2px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            "padding-bottom":"24px",
            "padding-top":"24px",

            'fontSize': '32px'  # Optionally increase the font size
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(
        id='output-image-upload',
        style={"width": "100%", "text-align": "center"}  # Center align content
    )
])


@app.callback(
    Output('output-image-upload', 'children'),
    [Input('upload-image', 'contents')],
    [State('upload-image', 'filename'), State('upload-image', 'last_modified')]
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        # Here you would process the image and determine if it's recyclable
        # This is just a placeholder logic
        is_recyclable = True  # Replace with actual image processing result
        children = [
            html.Div([
                html.Img(
                    src=list_of_contents[0],
                    style={'maxHeight': '300px', 'maxWidth': '300px'}
                ),
                html.H3('Result:', className='Recyclable'),
                # Display the result with an icon
                html.Div(
                    className='result-output',
                    children=[
                        html.Span('✅  Recyclable', className='recyclable',style={"text-align":"center"}) if is_recyclable else 
                        html.Span('❌ Not Recyclable', className='not-recyclable')
                    ]
                )
            ])
        ]
        return children
    raise PreventUpdate
