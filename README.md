Indian Air Quality Intelligence

An exploratory data analysis and machine learning project investigating air pollution patterns using Python, pandas, Matplotlib, and scikit-learn.

Project Overview

This project explores air-quality sensor data and Indian air-pollution measurements through data cleaning, exploratory analysis, visualization, and regression modelling.

Part 1: Air Quality Sensor Analysis

Dataset: UCI Air Quality dataset, containing approximately 9,357 observations and 15 columns.

Work completed:

* Loaded and inspected the dataset.
* Identified and handled missing values.
* Visualized pollutant measurements and relationships between variables.
* Built a linear regression model to predict benzene concentration.
* Tested polynomial regression and compared model performance using a chronological train-test split.

Preliminary results:

* Linear Regression: MAE ≈ 1.1243; R² ≈ 0.9466.
* Polynomial Regression (degree 2): MAE ≈ 0.0617; R² ≈ 0.9998.

These are preliminary results on this dataset and require further validation before any real-world predictive use.

Part 2: Delhi PM2.5 Analysis

This part analyzes PM2.5 measurements from five selected monitoring stations in Delhi for November 2024.

Stations included:

* Anand Vihar
* Bawana
* Ashok Vihar
* Alipur
* Aya Nagar

Work completed:

* Retrieved Indian air-quality data through an API.
* Examined daily PM2.5 averages and data coverage.
* Compared pollution levels across the five selected stations.
* Created visualizations and station-level summary statistics.
* Exported the analysis results to CSV files.

Key Findings

* Anand Vihar had the highest monthly average PM2.5 among the five selected stations, at approximately 308.72 µg/m³.
* Bawana followed at approximately 308.13 µg/m³.
* Aya Nagar had the lowest monthly average among the selected stations, at approximately 222.52 µg/m³.
* Each station had daily averages for all 30 days in November 2024.

These findings apply only to the selected stations and period; they should not be interpreted as a complete assessment of Delhi’s air quality.

Repository Contents

* indian_air_quality_analysis.ipynb — notebook containing the analysis.
* delhi_pm25_november_2024_all_stations.csv — daily PM2.5 data for the selected stations.
* delhi_pm25_november_2024_station_summary.csv — summary statistics for the selected stations.

Tools and Technologies

* Python
* pandas
* NumPy
* Matplotlib
* scikit-learn
* Jupyter Notebook / Google Colab
* API-based data collection

Limitations and Future Work

* The Delhi analysis covers five selected stations and one month only.
* The original sensor dataset is from Italy, not India.
* The regression results require additional validation on unseen periods and comparison with simple baselines.
* Future improvements include longer-term Indian air-quality analysis, additional stations, and more robust predictive modelling.

Project Status

Exploratory analysis completed for the initial sensor dataset and the selected Delhi PM2.5 observations. Further validation and development are ongoing.
