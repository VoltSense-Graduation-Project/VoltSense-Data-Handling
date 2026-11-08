# %% 
import pandas as pd

# %%
path = "../Data/Aruba/labeled/hh101.csv"


# %% 
with open(path) as f:
    for _ in range(10):
        print(repr(f.readline()))


# %%
df = pd.read_csv(path, header=None, engine="python", on_bad_lines="skip")
print(df.shape)
print(df.head(10))
print(df.nunique())


# %%
for i, activity in enumerate(df.iloc[:, 4].unique(), start=1):
    print(f"{i}. {activity}")

# %%
