import pandas as pd

# =============================================================================
# LOAD DATASET
# =============================================================================

df = pd.read_csv("data/AB_NYC_2019.csv")

print("Dataset Loaded Successfully")
print("-" * 50)

# =============================================================================
# BASIC INFORMATION
# =============================================================================

print("\nShape of Dataset:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nSummary Statistics:")
print(df.describe())

# =============================================================================
# DATA CLEANING
# =============================================================================

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing values in text columns
df.fillna({
    "name": "Unknown",
    "host_name": "Unknown"
}, inplace=True)

# Fill missing numerical values
df["reviews_per_month"] = df["reviews_per_month"].fillna(
    df["reviews_per_month"].mean()
)

# Convert last_review to datetime
df["last_review"] = pd.to_datetime(
    df["last_review"],
    errors="coerce"
)

# =============================================================================
# REMOVE INVALID VALUES
# =============================================================================

# Price should be greater than 0
df = df[df["price"] > 0]

# Minimum nights should be greater than 0
df = df[df["minimum_nights"] > 0]

# Availability should be between 0 and 365
df = df[
    (df["availability_365"] >= 0) &
    (df["availability_365"] <= 365)
]

# =============================================================================
# OUTLIER DETECTION (PRICE)
# =============================================================================

Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

print("\nPrice Outlier Limits")
print(f"Lower Bound : {lower_bound}")
print(f"Upper Bound : {upper_bound}")

outliers = df[
    (df["price"] < lower_bound) |
    (df["price"] > upper_bound)
]

print(f"Number of Outliers : {len(outliers)}")

# Remove outliers
df = df[
    (df["price"] >= lower_bound) &
    (df["price"] <= upper_bound)
]

# =============================================================================
# FINAL DATASET CHECK
# =============================================================================

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nRemaining Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFinal Data Types:")
print(df.dtypes)

# =============================================================================
# SAVE CLEANED DATASET
# =============================================================================

df.to_csv("AB_NYC_2019_Cleaned(1).csv", index=False)

print("\nData Cleaning Completed Successfully!")
print("Cleaned dataset saved as 'AB_NYC_2019_Cleaned.csv'")