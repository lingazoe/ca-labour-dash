import pandas as pd
import streamlit as st

def load_data(file):

    try:
        return pd.read_csv(file)
    except Exception as e:
        print(f"There was an error loading the file: {e}")
        return None

def format_dates(stats_df):

    stats_df['REF_DATE'] = pd.to_datetime(stats_df['REF_DATE'])

    return stats_df

def filter_unnecessary(stats_df):

    return stats_df.dropna(subset=['VALUE'])

def filter_cols(stats_df):

    cols = ['REF_DATE','Labour force characteristics','Educational attainment','Gender','Age group','VALUE']
    return stats_df[cols]

@st.cache_data
def get_data(stats_df):

    stats_df = load_data(stats_df)
    stats_df = format_dates(stats_df)
    stats_df = filter_unnecessary(stats_df)
    stats_df = filter_cols(stats_df)

    return stats_df