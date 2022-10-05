from exploratory_data_analysis.reading import read_data
from preprocessing.cleaning import impute_alley_missing_values, impute_missing_values

import pandas as pd

if __name__ == '__main__':
    data = read_data(url="data/train.csv")

    # Drop columns
    data_clean = data.drop(labels=["Utilities"], axis=1)

    # Impute missing values
    data_clean = impute_missing_values(data=data_clean, column="LotFrontage")
    data_clean = impute_alley_missing_values(data=data_clean)

    # Datatype casting
    data_clean["LotFrontage"] = data_clean["LotFrontage"].astype(int)
    data_clean["LotArea"] = data_clean["LotArea"].astype(int)

    # Encoders
    data_clean = pd.get_dummies(data=data_clean,
                                prefix=["MSZoning", "Street", "Alley", "LotShape", "LandContour"],
                                columns=["MSZoning", "Street", "Alley", "LotShape", "LandContour"])
    print(data_clean)
