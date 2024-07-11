import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset from GitHub
url = 'https://raw.githubusercontent.com/JoshJohann/mapping/main/walmart_data_geocoded.csv'
us_cities = pd.read_csv(url)

# Streamlit app
st.title('US Locations Map')

# Create filter options for businessUnit_status_code
status_codes = us_cities['businessUnit_status_code'].unique()
selected_status_codes = st.multiselect('Select Business Unit Status Code(s)', status_codes, default=status_codes)

# Create filter options for states
states = us_cities['State'].unique()
selected_states = st.multiselect('Select State(s)', states, default=states)

# Create filter options for Fuel Station open to public
fuel_station_options = us_cities['Fuel Station open to public'].unique()
selected_fuel_station_options = st.multiselect('Select Fuel Station Open to Public Option(s)', fuel_station_options, default=fuel_station_options)

# Filter data based on selections
filtered_data = us_cities[
    (us_cities['businessUnit_status_code'].isin(selected_status_codes)) &
    (us_cities['State'].isin(selected_states)) &
    (us_cities['Fuel Station open to public'].isin(selected_fuel_station_options))
]

# Create the Plotly map
fig = px.scatter_mapbox(filtered_data, lat="latitude", lon="longitude", hover_name="City", hover_data=["State", "Address"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=600)

fig.update_layout(mapbox_style="carto-darkmatter")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Show the map in the Streamlit app
st.plotly_chart(fig)
