import pandas as pd


def impute_alley_missing_values(data: pd.DataFrame):
    alley = data["Alley"]
    alley = alley.fillna("No")
    data["Alley"] = alley
    return data


# TODO: predict the missing values, not impute by the mean
def impute_missing_values(data: pd.DataFrame, column: str):
    data[column] = data[column].fillna(data[column].mean())
    return data
