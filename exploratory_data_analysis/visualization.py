import pandas as pd
import matplotlib.pyplot as plt

from reading import read_data

data = read_data(url="../data/train.csv")


def paint_hist(x, bins: int):
    plt.hist(x, bins=bins)
    plt.show()


def paint_bar(x):
    count_values = x.value_counts()
    d = pd.Series.to_dict(count_values)
    plt.bar(x=d.keys(), height=d.values())
    plt.show()


