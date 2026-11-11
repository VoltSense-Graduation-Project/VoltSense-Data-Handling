# %% Imports
from classes.DataAnalyzer import DataQualityAnalyzer
import pandas as pd
import csv
from pprint import pprint
from pathlib import Path


# %% Configuration
dataPath = Path("../../Data/adl_multipleresident/adl_multipleresident")
outputPath = Path("../../Adl-MultiResident-Processed")

outputPath.mkdir(parents=True, exist_ok=True)


# %% 
for path in dataPath.glob("*.csv"):

    with open(path, mode="r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    columnCounts = pd.Series([len(row) for row in rows])

    print(
        f"{path.name}: "
        f"{columnCounts.value_counts().to_dict()}"
    )


# %% Read and inspect CSV files
for path in dataPath.glob("*.csv"):

    with open(path, mode="r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    df = pd.DataFrame(
        rows,
        columns=[
            'Date', 'Time', 'Sensor', 'Message',
            'Performer1', 'Task1', 'Performer2', 'Task2'
        ]
    ).fillna(0)

    print(f"\nFile: {path.name}")
    print(df.head())
    print(df.tail())









































# %% Processing
# tasks = sorted({
#     path.name.split(".")[-2]
#     for path in dataPath.glob("*.csv")
# })

# for task in tasks:
#     paths = dataPath.glob(f"*.{task}.csv")

#     df = pd.concat(
#         [pd.read_csv(path) for path in paths],
#         ignore_index=True
#     )

#     df["Task"] = task

#     print(f"\n{'='*20} {task.upper()} {'='*20}")
#     print("Shape:", df.shape)

#     qualityAnalyzer = DataQualityAnalyzer(df)
#     pprint(qualityAnalyzer.generate_quality_report())

#     outputFile = outputPath / f"{task}.csv"
#     df.to_csv(outputFile, index=False)

#     print(f"Saved: {outputFile}")


# # %%