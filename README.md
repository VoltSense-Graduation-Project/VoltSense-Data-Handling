# VoltSense – Data Handling

**Data Collection, Exploration, Preprocessing, and Preparation for Smart Home Activity Recognition**

## Overview

This repository contains the data handling component of **VoltSense**, a smart home graduation project focused on understanding household activities and enabling intelligent home automation.

The primary purpose of this repository is to explore, assess, clean, and prepare smart home datasets for subsequent machine learning tasks.

It provides a structured workspace for working with sensor-based activity datasets, examining their quality and consistency, and transforming raw data into formats suitable for further analysis and model development.

## Objectives

- Explore and understand available smart home datasets.
- Assess data quality, structure, completeness, and consistency.
- Identify missing values, inconsistent records, and formatting issues.
- Preprocess and standardize sensor event data.
- Organize processed datasets for downstream machine learning workflows.
- Prepare data for smart home activity recognition experiments.

## Repository Structure

```text
VoltSense-Data-Handling/
│
├── Adl-NoError-Processed/
│   └── Processed ADL dataset files
│
├── Scripts/
│   └── Data exploration and preprocessing scripts
│
├── Datasets_Report.pdf
│
└── README.md
```

### Directories and Files

| Path | Description |
|---|---|
| `Adl-NoError-Processed/` | Contains processed files from the ADL NoError dataset. |
| `Scripts/` | Contains scripts used for dataset exploration, quality assessment, and preprocessing. |
| `Datasets_Report.pdf` | Documentation and analysis of the datasets considered for the project. |

## Datasets

VoltSense works with smart home datasets containing sensor events and activity-related information.

These datasets provide information about household environments through sensor readings, event timestamps, and activity annotations.

One of the datasets currently included in the workflow is the **ADL NoError dataset**, which provides sensor event records associated with activities of daily living.

The data is used to investigate relationships between sensor events and household activities, providing a foundation for future activity recognition models.

## Data Processing Workflow

The data handling process follows a structured workflow:

1. **Data Exploration**
   - Inspect dataset structures and dimensions.
   - Understand available attributes and data types.
   - Examine sensor events and activity annotations.

2. **Data Quality Assessment**
   - Identify missing and inconsistent values.
   - Investigate malformed records.
   - Examine structural inconsistencies across files.
   - Evaluate dataset completeness.

3. **Data Cleaning**
   - Address formatting inconsistencies.
   - Handle missing or malformed records where appropriate.
   - Standardize data representation.

4. **Data Preprocessing**
   - Organize and transform dataset records.
   - Standardize processed files.
   - Prepare datasets for subsequent analysis and machine learning.

5. **Dataset Preparation**
   - Store processed datasets in an organized structure.
   - Make the resulting data accessible for downstream experiments.

## Technologies

The repository primarily uses Python and its data processing ecosystem.

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data manipulation and preprocessing |
| NumPy | Numerical operations |
| Jupyter / Python Scripts | Experimentation and data exploration |

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/VoltSense-Graduation-Project/VoltSense-Data-Handling.git

cd VoltSense-Data-Handling
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install pandas numpy jupyter
```

Additional dependencies may be required depending on the script being executed.

### 4. Explore the Repository

Start by examining the scripts inside the `Scripts/` directory and the available processed datasets.

## Project Context

VoltSense aims to bring intelligence into everyday home environments by combining smart home technologies, sensor data, and machine learning.

Reliable data preparation is an essential part of this process. The quality and consistency of the input data directly influence the reliability of subsequent analysis and machine learning models.

This repository focuses specifically on the data handling stage of the project.

## Project Status

**Development in Progress**

The repository is part of the ongoing VoltSense graduation project. Dataset exploration, quality assessment, and preprocessing are being developed iteratively as the project progresses.

---

**VoltSense Graduation Project**
