from connection import KaggleDatasetConnection
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Taylor Swift's Spotify data")

st.title("Taylor Swift's Spotify data")

conn = st.experimental_connection("kaggle_datasets", type=KaggleDatasetConnection)
df = conn.get(path='thespacefreak/taylor-swift-spotify-data', filename='spotify_taylorswift.csv', ttl=3600)

st.dataframe(df)