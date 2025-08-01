# Gezinomi Sales Data Analysis

## 📋 Overview

This project presents a comprehensive analysis of sales data from Gezinomi, a travel agency. The primary goal is to explore sales patterns, understand customer behavior, and apply rule-based segmentation to create data-driven customer personas. The analysis delves into how factors like city, hotel concept, and booking season influence sales prices.

This project was completed as part of the Python Programming for Data Science module in the Data Scientist Path training program by [Miuul](https://miuul.com).

## 📊 Dataset

Please note: Due to licensing and privacy restrictions, the dataset (`miuul_gezinomi.xlsx`) used in this analysis is **not included** in this repository.

To run the analysis, you must provide your own version of the dataset and place it in the `gezinomi_project/` directory. The dataset should contain the following key columns:

* `SaleCityName`: The city where the sale was made.
* `ConceptName`: The concept of the hotel (e.g., "All-Inclusive").
* `Price`: The price of the sale.
* `SaleCheckInDayDiff`: The number of days between the sale date and the check-in date.
* `Seasons`: The travel season (e.g., "High", "Low").
* `CInDay`: The day of the week for check-in.

## 🚀 Key Analyses and Features

This project answers several key business questions and develops new features to enhance the analysis:

### Analysis Highlights
* Calculated sales frequencies and total revenue by city.
* Analyzed sales performance across different hotel concepts.
* Determined average prices based on various breakdowns (City, Concept, Season).
* Grouped and aggregated data to reveal deeper insights into pricing structures.

### Feature Engineering & Persona Creation
1.  **`EB_Score` (Early Booker Score)**: A categorical feature was created to segment customers based on how far in advance they book their vacation. Segments include:
    * Last Minuters (0-7 days)
    * Potential Planners (7-30 days)
    * Planners (30-90 days)
    * Early Bookers (90+ days)

2.  **`sales_level_based` (Personas)**: Rule-based customer personas were defined by combining `City`, `Concept`, and `Season`. This creates specific, actionable customer profiles (e.g., `ANTALYA_HERŞEY DAHIL_HIGH`).

3.  **`SEGMENT`**: The newly created personas were segmented into four distinct tiers (A, B, C, D) based on their average sales price. This allows for easy identification of high-value and low-value customer groups.

## 🛠️ Technologies Used

* **Python**
* **Pandas**: For data manipulation and analysis.
* **NumPy**: For numerical operations.
* **Matplotlib** & **Seaborn**: For data visualization.
* **Jupyter Notebook**: As the main development environment.

4.  **Run the analysis:**
    Open and run the `gezinomi_analysis.ipynb` notebook in a Jupyter environment to see the full analysis, from data loading to persona segmentation and insights.
