from streamlit.connections import ExperimentalBaseConnection
import os
import pandas as pd
import zipfile
import streamlit as st


class KaggleDatasetConnection(ExperimentalBaseConnection):

    def _connect(self):
        # Set Kaggle credentials
        os.environ['KAGGLE_USERNAME'] = st.secrets.KAGGLE_USERNAME
        os.environ['KAGGLE_KEY'] = st.secrets.KAGGLE_KEY

        # importing here because it requires the credentials to be set
        from kaggle.api.kaggle_api_extended import KaggleApi

        # Initialize Kaggle API connection
        self.conn = KaggleApi()

    def get(self, path, filename, ttl):
        @st.cache_data(ttl=ttl)
        def _get(path=path):
            # Authenticate to Kaggle
            self.conn.authenticate()
            # Download zip file
            self.conn.dataset_download_files(path)
            # get filename from path
            file_name = path.split('/')[-1] + ".zip"
            # Dataset is downloaded as a zip, so we need to extract it
            with zipfile.ZipFile(file_name, 'r') as zip_ref:
                zip_ref.extractall('.')
            # Read csv file to df
            df = pd.read_csv(filename)
            return df
        return _get(path)



