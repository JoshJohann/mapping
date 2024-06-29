import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset from GitHub
url = 'https://raw.githubusercontent.com/JoshJohann/mapping/main/walmart_data_geocoded.csv'
us_cities = pd.read_csv(url)

# Streamlit app
st.title('US Locations Map')

# Create filter options for states
states = us_cities['State'].unique()
selected_states = st.multiselect('Select State(s)', states, default=states)

# Filter data based on selected states
filtered_data = us_cities[us_cities['State'].isin(selected_states)]

# Create filter options for cities within the selected states
cities = filtered_data['City'].unique()
selected_cities = st.multiselect('Select City(ies)', cities, default=cities)

# Filter data based on selected cities
final_data = filtered_data[filtered_data['City'].isin(selected_cities)]

# Create the Plotly map
fig = px.scatter_mapbox(final_data, lat="latitude", lon="longitude", hover_name="City", hover_data=["State", "Address"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=600)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Show the map in the Streamlit app
st.plotly_chart(fig)
