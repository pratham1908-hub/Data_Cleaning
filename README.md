# 🧹 Data Cleaning & Preprocessing — Airbnb NYC Dataset

> **Oasis Infobyte Data Analytics Internship | Project 3 | Level 1**

---

## 📌 Project Overview

This project demonstrates a complete **data cleaning and preprocessing pipeline** applied to the Airbnb New York City 2019 dataset (`AB_NYC_2019.csv`). The goal is to transform raw, messy data into a clean, analysis-ready dataset using Python and Pandas.

---

## 📂 Dataset

| Property | Details |
|----------|---------|
| **File** | `AB_NYC_2019.csv` |
| **Source** | [Inside Airbnb](http://insideairbnb.com/) |
| **Rows** | 48,895 |
| **Columns** | 16 |
| **Domain** | Airbnb listings across NYC's 5 boroughs (2019) |

---

## 🛠️ Tools & Libraries

```
Python 3.x
├── pandas       → Data loading, inspection, transformation
├── numpy        → Numerical operations, IQR outlier detection
├── matplotlib   → Visualisation (boxplots, missing value heatmaps)
└── VS Code      → Development environment
```

---

## 🗂️ Project Structure

```
data-cleaning-airbnb/
│
├── AB_NYC_2019.csv               # Raw dataset (input)
├── AB_NYC_2019_cleaned.csv       # Cleaned dataset (output)
├── data_cleaning.py              # Main cleaning script
├── Data_Cleaning_Project_Report.pdf  # Full project report
└── README.md                     # This file
```

---

## 🔄 Cleaning Pipeline

```
Load Data → Inspect Structure → Detect Missing Values
    → Handle Missing Values → Remove Duplicates
    → Validate Data Types → Detect Outliers
    → Export Cleaned Dataset
```

### Phase-by-Phase Breakdown

| Phase | Task | Method |
|-------|------|--------|
| 1 | Load dataset | `pd.read_csv()` |
| 2 | Structural inspection | `df.info()`, `df.shape`, `df.head()` |
| 3 | Missing value detection | `df.isnull().sum()` |
| 4 | Handle missing values | Fill / retain strategy |
| 5 | Duplicate removal | `df.drop_duplicates()` |
| 6 | Data type validation | `df.dtypes`, casting |
| 7 | Outlier detection | IQR method on `price` |
| 8 | Export clean data | `df.to_csv()` |

---

## 🔍 Missing Values — Analysis & Strategy

| Column | Missing | % | Strategy |
|--------|---------|---|----------|
| `name` | 16 | 0.03% | Fill with `'Unknown'` |
| `host_name` | 21 | 0.04% | Fill with `'Unknown'` |
| `reviews_per_month` | 10,052 | 20.56% | Fill with `0` |
| `last_review` | 10,052 | 20.56% | Retain as `NaT` (intentional) |

> **Note:** `last_review` is intentionally left null — its absence means the listing has never been reviewed. Imputing a date would be semantically incorrect.

---

## ⚙️ Key Code Snippets

### Load & Inspect
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('AB_NYC_2019.csv')
print(df.shape)       # (48895, 16)
print(df.info())
print(df.isnull().sum())
```

### Handle Missing Values
```python
df['name'].fillna('Unknown', inplace=True)
df['host_name'].fillna('Unknown', inplace=True)
df['reviews_per_month'].fillna(0, inplace=True)
# last_review — intentionally left as NaT
```

### Remove Duplicates
```python
print(f"Duplicates: {df.duplicated().sum()}")
df.drop_duplicates(inplace=True)
```

### Outlier Detection (IQR)
```python
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df['price'] < lower) | (df['price'] > upper)]
print(f"Outliers detected: {len(outliers)}")
```

### Export Cleaned Data
```python
df.to_csv('AB_NYC_2019_cleaned(1).csv', index=False)
print("Cleaned dataset saved!")
```

---

## 📊 Results Summary

| Metric | Before | After |
|--------|--------|-------|
| Total Rows | 48,895 | 48,895 |
| Duplicate Rows | 0 | 0 |
| Missing: `name` | 16 | 0 |
| Missing: `host_name` | 21 | 0 |
| Missing: `reviews_per_month` | 10,052 | 0 |
| Missing: `last_review` | 10,052 | 10,052 (retained) |
| Price = $0 listings | Present | Flagged/Removed |
| Data Types Correct | Partial | Fully Validated |

---

## 💡 Key Concepts Covered

- **Data Integrity** — Ensuring logical consistency across all columns
- **Missing Data Handling** — Domain-aware imputation strategies
- **Duplicate Removal** — Preventing inflated statistics
- **Standardisation** — Consistent types and formats for modelling
- **Outlier Detection** — IQR-based method on numerical columns

---

## 🚀 Future Scope

- [ ] Exploratory Data Analysis (EDA) with borough-wise visualisations
- [ ] Feature engineering from `last_review` (extract month/year)
- [ ] Price prediction model (Linear Regression / Random Forest)
- [ ] NLP on listing `name` column for sentiment/keyword extraction
- [ ] Neighbourhood clustering using K-Means

---

## 👤 Author

**Pratham**
Data Analytics Internship — Oasis Infobyte
Project 3 | Level 1 | Data Cleaning

---

*Dataset source: [Inside Airbnb](http://insideairbnb.com/) — Open data for Airbnb listings.*
