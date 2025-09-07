# sales_analysis.py
# Sales Dataset Analysis
# Author: Mainuu
# ---------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Enable seaborn style
sns.set(style="whitegrid")

# --------------------------
# Task 1: Load and Explore the Dataset
# --------------------------
try:
    df = pd.read_csv("sales_dataset.csv", parse_dates=["Date"])
    print("Dataset successfully loaded.\n")
except FileNotFoundError:
    print("Error: File 'sales_dataset.csv' not found. Please check the path.")
    exit()
except Exception as e:
    print(f"Error reading the dataset: {e}")
    exit()

# Display first rows
print("First 5 rows of dataset:")
print(df.head(), "\n")

# Dataset structure
print("Dataset Info:")
print(df.info(), "\n")

# Summary statistics
print("Summary Statistics:")
print(df.describe(include="all"), "\n")

# Missing values
print("Missing Values:")
print(df.isnull().sum(), "\n")

# Handle missing values if any
if df.isnull().values.any():
    df = df.fillna({
        col: 0 if df[col].dtype in ['int64', 'float64'] else "Unknown"
        for col in df.columns
    })
    print("Missing values filled.\n")

# --------------------------
# Task 2: Basic Data Analysis
# --------------------------
print("Basic Statistics for Numerical Columns:")
print(df.describe().T, "\n")

# Groupings
region_sales_mean = df.groupby("Region")["Total"].mean()
print("Average Sales (Total) by Region:")
print(region_sales_mean, "\n")

product_quantity_mean = df.groupby("Product")["Quantity"].mean()
print("Average Quantity Sold by Product:")
print(product_quantity_mean, "\n")

# --------------------------
# Task 3: Data Visualization
# --------------------------

# 1. Line Chart - Sales Trend Over Time
plt.figure(figsize=(8, 5))
sns.lineplot(x="Date", y="Total", data=df, estimator="sum", marker="o")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Bar Chart - Average Sales by Region
plt.figure(figsize=(6, 5))
sns.barplot(x="Region", y="Total", data=df, estimator="mean", palette="Blues_d")
plt.title("Average Sales by Region")
plt.xlabel("Region")
plt.ylabel("Average Sales ($)")
plt.tight_layout()
plt.show()

# 3. Histogram - Price Distribution
plt.figure(figsize=(6, 5))
sns.histplot(df["Price"], bins=8, kde=True, color="orange")
plt.title("Distribution of Product Prices")
plt.xlabel("Price ($)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4. Scatter Plot - Quantity vs Total Sales
plt.figure(figsize=(6, 5))
sns.scatterplot(x="Quantity", y="Total", hue="Product", data=df, palette="Set2", s=100)
plt.title("Quantity vs. Total Sales by Product")
plt.xlabel("Quantity Ordered")
plt.ylabel("Total Sales ($)")
plt.legend(title="Product")
plt.tight_layout()
plt.show()

# --------------------------
# Task 4: Findings / Observations
# --------------------------
print("Findings / Observations:")
print("- Tablets generated the highest total sales, showing strong demand.")
print("- The West region showed very high sales from Headphones orders.")
print("- Monitor sales are spread across all regions with steady but smaller contributions.")
print("- South region had frequent sales but at lower price points compared to other regions.")
print("- Scatter plot shows higher Total values for Tablets and Headphones, regardless of Quantity.")
