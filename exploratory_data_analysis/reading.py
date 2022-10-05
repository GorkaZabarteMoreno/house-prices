import pandas as pd


def read_data(url: str):
    return pd.read_csv(filepath_or_buffer=url)
