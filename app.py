import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset from GitHub
url = 'https://raw.githubusercontent.com/JoshJohann/mapping/main/walmart_data_geocoded.csv'
us_cities = pd.read_csv(url)

# Streamlit app
st.title('US Locations Map')

# Create the Plotly map
fig = px.scatter_mapbox(us_cities, lat="latitude", lon="longitude", hover_name="City", hover_data=["State"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=600)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Show the map in the Streamlit app
st.plotly_chart(fig)
