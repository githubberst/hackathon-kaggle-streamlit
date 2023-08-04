from connection import KaggleDatasetConnection
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Kaggle-Streamlit Connection Demo App")

st.title("Kaggle-Streamlit Connector App")

st.info('This is a demo app that presents basic use of custom Kaggle-Streamlit connector built using ExperimentalBaseConnection')

conn = st.experimental_connection("kaggle_datasets", type=KaggleDatasetConnection)
# df = conn.get(path='gayu14/taylor-concert-tours-impact-on-attendance-and', filename='Taylor_Train.csv', ttl=3600)
file_object = conn.get(path='gayu14/taylor-concert-tours-impact-on-attendance-and', filename='Taylor_Train.csv', ttl=3600)
df = pd.read_csv(file_object, encoding='latin-1') 