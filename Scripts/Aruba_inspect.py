# %% 
import pandas as pd


# %%
from pathlib import Path

dataPath = Path("../Data/Aruba/data")

paths = [
    dataPath / file
    for file in ["aruba.csv", "atmo1.csv", "cairo.csv", "hh101.csv", "ihs06.csv", "kyoto07.csv"]
]


# %% 
for path in paths:
    with open(path) as f:
        for _ in range(10):
            print(repr(f.readline()))

    df = pd.read_csv(path, header=None)
    print(df.shape)
    print(df.head(10))
    print(df.nunique())
    print()
    print()
    print()

# %%
