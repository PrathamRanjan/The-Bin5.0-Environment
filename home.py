from dash import html, dcc

# Define the layout for the home page
def create_layout():
    return html.Div([
        html.Section([
            html.Div([
                html.H2('Recycling News', className='recycling-news-heading'),  # Heading for the news section
                html.Div([  # This div contains the first news card
                    html.Img(src='assets/sg.jpg', className='news-image'),
                    html.H3('Recycled Carbon',style={"text-align":"center"}),
                    html.P('Singapore-based company Nandina REM debuts recycled carbon.',style={"text-align":"center"}),
                    dcc.Link('Read More', href='https://www.businesstimes.com.sg/companies-markets/transport-logistics/singapore-based-company-nandina-rem-debuts-recycled-carbon', className='read-more'),
                ], className='news-card'),

                html.Div([  # This div contains the second news card
                    html.Img(src='assets/fashion.jpg', className='news-image'),
                    html.H3('Fashion Recycling',style={"text-align":"center"}),
                    html.P('Why fashion’s recycling is not saving the planet.',style={"text-align":"center"}),
                    dcc.Link('Read More', href='https://www.businesstimes.com.sg/esg/why-fashions-recycling-not-saving-planet', className='read-more'),
                ], className='news-card'),

                html.Div([  # This div contains the third news card
                    html.Img(src='assets/recycling10.jpg', className='news-image'),
                    html.H3('American Recycle System',style={"text-align":"center"}),
                    html.P('Americans throw three-quarters of their recyclables into the trash.',style={"text-align":"center"}),
                    dcc.Link('Read More', href='https://www.businesstimes.com.sg/esg/americans-throw-three-quarters-their-recyclables-trash', className='read-more'),
                ], className='news-card'),

                html.Div([  # This div contains the fourth news card
                    html.Img(src='assets/battery.jpg', className='news-image'),
                    html.H3('Recyclable Batteries',style={"text-align":"center"}),
                    html.P('Utilisation of Recyclable Batteries for cars.',style={"text-align":"center"}),
                    dcc.Link('Read More', href='https://www.businesstimes.com.sg/international/global/electric-cars-recycled-batteries-are-next-green-holy-grail', className='read-more'),
                ], className='news-card'),
                html.H2('Recycling Statistics', className='recycling-news-heading'),  # Heading for the news section
                html.Div([  # This div contains the first news card
                    html.Img(src='assets/Visual1.png', className='stats-image'),
                    html.H3('Personal Waste and Recycling Statistics'),
                ], className='stats-card'),
                html.Div([  # This div contains the first news card
                    html.Img(src='assets/Visual2.png', className='stats-image'),
                    html.H3('UserActivity'),
                ], className='stats-card')


            ], className='news-container')
        ], className='recycling-news-section'),
    ], className='home-container')

layout = create_layout()