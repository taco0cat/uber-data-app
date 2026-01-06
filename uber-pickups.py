import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# Set the title for the web app
st.set_page_config(page_title="Uber NYC", page_icon="🚕")

st.title("Uber Pickups in NYC")

# Fetching Data
DATE_COLUMN = 'date/time'
DATA_URL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

# Caching Data to Speed Up Load Times
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.index = range(1, nrows+1)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000) # Load 10,000 Rows of Data
data_load_state.text("Data Fetched! (using st.cache_data)")

if st.checkbox('Show Raw Data'):
    st.subheader("Raw Data")
    st.write(data)

st.subheader("Number of pickups by hour")

# Generate Histogram Data
@st.cache_data
def get_histogram(df_column):
    return np.histogram(df_column.dt.hour, bins=24, range=(0, 24))[0]

hist_values = get_histogram(data[DATE_COLUMN])
st.bar_chart(hist_values)

# Plotting Pickup Locations on a Map (Filtered by Hour)
hour_to_filter = st.slider('Hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

# Adding a chart Using PyDeck
st.subheader(f'3D Map of all pickups at {hour_to_filter}:00')
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=40.7128,
        longitude=-74.0060,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=filtered_data,
            get_position='[lon, lat]',
            radius=100,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
        ),
    ],
))