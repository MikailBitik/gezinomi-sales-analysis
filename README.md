Gezinomi Customer Segmentation Project
Overview
This project focuses on customer segmentation and revenue prediction based on travel booking data from Gezinomi, a Turkish travel agency. The aim is to derive actionable insights by analyzing user behavior, booking timing, seasonal patterns, and city-concept combinations. The analysis results in the creation of customer personas and segmentation for revenue estimation.

This project was completed as part of the Python Programming for Data Science module in the Data Scientist Path training program by Miuul.

Dataset Description
The dataset contains information about travel bookings, including:

SaleCityName: City where the sale was made

ConceptName: Type of service or accommodation package

Price: Amount paid for the booking

SaleCheckInDayDiff: Days between booking and check-in

Seasons: Season of travel

CInDay: Day of check-in

Key Tasks & Insights
1. Data Exploration
Identified the number of unique cities and concepts.

Calculated frequency distributions and total revenue per city and concept.

Analyzed average prices across different city and concept combinations.

2. Booking Timing Categorization
Created a new feature (EB_Score) based on how early a booking was made:

Last Minuters (0–7 days)

Potential Planners (8–30 days)

Planners (31–90 days)

Early Bookers (91+ days)

3. Multi-level Aggregations
Explored metrics such as mean price and transaction count across:

City-Concept-Booking Timing (EB_Score)

City-Concept-Season

City-Concept-Check-in Day

4. Persona Creation
Created new personas by combining city, concept, and season:

ini
Kodu kopyala
sales_level_based = SaleCityName_ConceptName_Seasons
Transformed these into uppercase for consistency.

5. Customer Segmentation
Segmented personas into 4 segments (A–D) based on average price using quantiles.

Described each segment by mean, max, and total price contribution.

6. Revenue Estimation for New Users
Estimated potential revenue from two sample users:

"ANTALYA_HERŞEY DAHIL_HIGH" — high-value customer in Segment A.

"GIRNE_YARIM PANSIYON_LOW" — lower-value customer in Segment C or D.

Technologies Used
Python

Pandas

NumPy

Seaborn

Matplotlib

Jupyter Notebook

How to Run
Make sure you have the required libraries installed:

bash
Kodu kopyala
pip install pandas numpy matplotlib seaborn openpyxl
Place the dataset in the correct path:
gezinomi_project/miuul_gezinomi.xlsx

Run the script or notebook to explore, preprocess, and analyze the data.

Author
This analysis was completed as part of the Miuul Data Scientist Path program.

License
This project is for educational purposes and is not intended for commercial use.

