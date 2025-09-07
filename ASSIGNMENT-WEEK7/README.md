


## 📌 Project Overview

This project analyzes a **sales dataset (`sales_dataset.csv`)** using Python.
The script performs:

1. **Data loading and exploration** (Task 1)
2. **Basic statistical analysis** (Task 2)
3. **Data visualization** (Task 3)
4. **Findings and observations** (Task 4)

Both **pandas**, **matplotlib**, and **seaborn** are used for data analysis and visualization.

---

## 📂 Files Included

* **`sales_dataset.csv`** → Input dataset containing sales records
* **`sales_analysis.py`** → Python script performing analysis and visualization
* **`README.md`** → Documentation file

---

## ⚙️ Requirements

Install dependencies before running the script:

```bash
pip install pandas matplotlib seaborn
```

---

## ▶️ How to Run the Script

1. Place **`sales_dataset.csv`** and **`sales_analysis.py`** in the same folder.
2. Run the script:

```bash
python sales_analysis.py
```

3. The script will:

   * Print dataset info, summary, and missing value checks
   * Display statistical analysis (mean, median, std, etc.)
   * Generate four different visualizations
   * Print key findings

---

## 📊 Visualizations

The script produces four charts:

1. **Line Chart** → Sales trend over time
2. **Bar Chart** → Average sales by region
3. **Histogram** → Distribution of product prices
4. **Scatter Plot** → Quantity vs. Total sales (colored by product)

---

## 🔎 Key Findings

* **Tablets** generated the highest total sales overall.
* **Headphones** in the **West region** contributed disproportionately due to high unit prices.
* **Monitor** sales were consistent but smaller across regions.
* **South region** had frequent sales but lower average prices compared to other regions.
* **Scatter plot** confirmed that Tablets and Headphones drove most of the high-value orders.

---

## 🛡️ Error Handling

* If `sales_dataset.csv` is missing, the script will display an error message and exit.
* If missing values exist, they are filled with `0` (for numeric columns) or `"Unknown"` (for categorical columns).

---
