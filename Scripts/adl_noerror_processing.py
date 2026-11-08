# %% Imports
from classes.DataAnalyzer import DataQualityAnalyzer
import pandas as pd
from pprint import pprint
from pathlib import Path


# %% Configuration
dataPath = Path("../Data/adl_noerror/adl_noerror")
outputPath = Path("../Adl-NoError-Processed")

outputPath.mkdir(parents=True, exist_ok=True)


# %% Processing
tasks = sorted({
    path.name.split(".")[-2]
    for path in dataPath.glob("*.csv")
})

for task in tasks:
    paths = dataPath.glob(f"*.{task}.csv")

    df = pd.concat(
        [pd.read_csv(path) for path in paths],
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


# %%