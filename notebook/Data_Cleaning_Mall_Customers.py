# 🔹 Project: Data Cleaning & Quality Report (Dirtydataset.CSV)
# Tools: Pandas, Matplotlib, Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
sns.set(style="whitegrid")

# Step 1: Upload your CSV
from google.colab import files
uploaded = files.upload()  # Select your Dirtydataset.CSV

# Step 2: Load dataset
dataset_path = 'Dirtydataset.CSV'  # Ensure filename matches
df = pd.read_csv(dataset_path)

# Step 3: Inspect dataset
print("First 5 rows:\n", df.head())
print("\nDataset info:\n")
df.info()
print("\nSummary statistics:\n", df.describe())

# Step 4: Detect missing values
missing = df.isnull().sum()
print("\nMissing values per column:\n", missing)

plt.figure(figsize=(8,5))
sns.heatmap(df.isnull(), cbar=False, cmap="YlOrRd")
plt.title("Missing Values Heatmap")
plt.show()

# Step 5: Detect duplicates
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

# Step 6: Detect outliers (numeric columns)
numeric_cols = df.select_dtypes(include=['int64','float64']).columns
for col in numeric_cols:
    plt.figure(figsize=(6,3))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()

# Step 7: Clean the data
# Drop duplicates
df_cleaned = df.drop_duplicates()

# Fill missing values: numeric -> mean, categorical -> mode
for col in df_cleaned.columns:
    if df_cleaned[col].dtype in ['int64','float64']:
        df_cleaned[col].fillna(df_cleaned[col].mean(), inplace=True)
    else:
        df_cleaned[col].fillna(df_cleaned[col].mode()[0], inplace=True)

# Step 8: Verify cleaning
print("\nMissing values after cleaning:\n", df_cleaned.isnull().sum())
print("Number of duplicates after cleaning:", df_cleaned.duplicated().sum())

# Step 9: Data Quality Report (summary statistics)
summary = df_cleaned.describe(include='all')
print("\nData Quality Report:\n", summary)

# Step 10: Save cleaned dataset and report
df_cleaned.to_csv('Dirtydataset_cleaned.csv', index=False)
summary.to_csv('Dirtydataset_data_quality_report.csv')

# Step 11: Plot distributions after cleaning
for col in numeric_cols:
    plt.figure(figsize=(6,3))
    sns.histplot(df_cleaned[col], kde=True, bins=15)
    plt.title(f"Distribution of {col} (after cleaning)")
    plt.show()

# Step 12: Download cleaned CSV and report
from google.colab import files
files.download('Dirtydataset_cleaned.csv')
files.download('Dirtydataset_data_quality_report.csv')

print("✅ Data cleaning complete. Cleaned dataset and report ready for download.")
