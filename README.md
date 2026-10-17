Indian Air Quality Intelligence

An exploratory data analysis and machine learning project using air-quality sensor data, built with Python.

Project Overview

This project explores relationships between air pollutants, studies sensor measurements, and develops a regression model to predict benzene concentration.

Current dataset: An air-quality dataset from Italy. The project will be extended to include Indian air-quality data.

Work Completed

* Loaded and inspected a dataset containing 9,357 observations and 15 columns.
* Examined missing values and cleaned the dataset.
* Visualized pollutant measurements over observations.
* Analyzed correlations between air pollutants.
* Built a regression model to predict benzene concentration.
* Evaluated the model using a chronological train-test split.

Preliminary Model Results

Metric	Result
Test MAE	1.124
Test R²	0.947

These are preliminary results for the current dataset and evaluation setup. Further validation is needed to check for data leakage and assess generalization.

Tools and Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Google Colab
* GitHub

Future Improvements

* Investigate missing-data handling and possible data leakage.
* Compare multiple regression models against a baseline.
* Improve time-aware model evaluation.
* Extend the analysis using Indian air-quality data.
* Develop an interactive dashboard for exploring pollution trends.

Project Status

In progress — developed as a learning project for Data Science and AI.
Model Performance

Two regression approaches were evaluated for predicting benzene concentration (C6H6(GT)) from the PT08.S2(NMHC) sensor response.

Model	Test MAE	Test R²
Linear Regression	1.125	0.947
Polynomial Regression (Degree 2)	0.06166	0.99979

Results

Polynomial Regression achieved substantially lower prediction error and a higher R² score than the linear baseline on the chronological test split.

Limitations

These results reflect performance on the available dataset. Further validation across different time periods and independent data is needed before claiming reliable real-world predictive performance.
