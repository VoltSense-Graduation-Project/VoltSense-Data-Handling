# %% Imports
from pathlib import Path


# %% Configuration
dataPath = Path("../Data/adl_interweave/adl_interweave")


# %% Convert to UTF-8
for path in dataPath.glob("*.csv"):

    content = path.read_bytes()

    if content.startswith((b"\xff\xfe", b"\xfe\xff")):
        content = content.decode("utf-16").encode("utf-8")

        path.write_bytes(content)

        print(f"Converted: {path.name}")

    else:
        print(f"Already UTF-8: {path.name}")


# %% Imports
from classes.DataAnalyzer import DataQualityAnalyzer
import pandas as pd
import csv
from pprint import pprint
from pathlib import Path


# %% Configuration
dataPath = Path("../Data/adl_interweave/adl_interweave")
outputPath = Path("../Adl-Interweave-Processed")

outputPath.mkdir(parents=True, exist_ok=True)


# %% Processing
tasks = sorted({
    path.name.split(".")[-2]
    for path in dataPath.glob("*.csv")
})

for task in tasks:
    paths = dataPath.glob(f"*.{task}.csv")

    df = pd.concat(
        [
            pd.read_csv(path, header=None, names=['date', 'time', 'sensor', 'message'])
            for path in paths
        ],
        ignore_index=True
    )

    df["Task"] = task

    print(f"\n{'='*20} {task.upper()} {'='*20}")
    print("Shape:", df.shape)

    qualityAnalyzer = DataQualityAnalyzer(df)
    pprint(qualityAnalyzer.generate_quality_report())

    outputFile = outputPath / f"{task}.csv"
    df.to_csv(outputFile, index=False)

    print(f"Saved: {outputFile}")


# %% Configuration
dataPath = Path("../Data/adl_interweave/adl_interweave/interwoven files")
outputPath = Path("../Adl-Interweave-Processed")

outputPath.mkdir(parents=True, exist_ok=True)


# %%
for path in dataPath.glob("*.csv"):

    with open(path, mode="r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    df = pd.DataFrame()

        
# %%
