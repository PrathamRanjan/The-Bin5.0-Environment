# apps/recycling_bins.py

from dash import html
import folium
from folium import IFrame
import geopandas as gpd
from shapely.geometry import Point

def create_map_layout(user_location):
    # Load the GeoJSON file containing the recycling bins
    file_path = 'RecyclingBins.geojson'  # Adjust the path as needed
    recycling_bins = gpd.read_file(file_path)

    # Convert user location to a Shapely Point (note the order of longitude and latitude)
    user_point = Point(user_location[1], user_location[0])

    recycling_bins['distance'] = recycling_bins.apply(
        lambda row: user_point.distance(row['geometry']),
        axis=1
    )

    nearest_bin = recycling_bins.loc[recycling_bins['distance'].idxmin()]

    m = folium.Map(location=[user_location[0], user_location[1]], zoom_start=15)

    folium.Marker(
        location=user_location,
        popup='Your Location',
        icon=folium.Icon(color='blue')
    ).add_to(m)



    nearest_bin_location = (nearest_bin.geometry.y, nearest_bin.geometry.x)
    folium.Marker(
        location=[nearest_bin_location[0], nearest_bin_location[1]],
        popup='Nearest Recycling Bin',
        icon=folium.Icon(color='green')
    ).add_to(m)

    # Save the map to an HTML string
    map_html = m._repr_html_()

    # Return a layout including the map inside an IFrame
    return html.Div([
        html.H1("Nearby Recycling Bins", style={'textAlign': 'center','color':'white'}),
        html.Iframe(
            srcDoc=map_html,
            width='100%',
            height='600px'
        ),
        html.Div(
            [
                html.Div([
                    html.Span(style={'color': 'darkgreen','font-size':'24px'}, children=[html.I(className="fa fa-arrow-up"), " Nearest Recycling Bin"]),
                    html.Br(),
                    html.Span(style={'color': 'midnightblue','font-size':'24px'}, children=[html.I(className="fa fa-arrow-up"), " Your Location"])
                ], style={
                    'border': '2px solid #ddd', 
                    'padding': '10px', 
                    'margin-top': '10px', 
                    'border-radius': '5px',
                    'text-align': 'center'
                })
            ],
            style={'textAlign': 'center'}
        )
    ])

# Set the user's location (hardcoded for the example)
latitude = 1.347509
longitude = 103.680842
user_location = [latitude, longitude]  

# Call the function to create the map layout
layout = create_map_layout(user_location)
