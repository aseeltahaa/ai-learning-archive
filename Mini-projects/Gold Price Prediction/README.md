# Gold Price Prediction

Predicts future gold prices using historical financial data and machine learning.

## Project Overview

**Problem:** Predict the price of gold based on historical market indicators
**Approach:** Regression using Machine Learning → Random Forest Regressor
**Dataset:** Historical gold price dataset with related financial features (e.g., USD index, oil prices, stock indices)

## Objectives

* Build an accurate model to predict gold prices
* Understand relationships between gold prices and economic indicators
* Practice a complete ML pipeline from data preprocessing to evaluation
* Explore ensemble learning methods (Random Forest)

## Dataset

* **Source:** Kaggle / Financial datasets (Gold price & related indicators)
* **Features:** Market indicators such as:

  * USD Index
  * Oil Prices
  * Stock Market Indices (e.g., S&P 500)
  * Interest Rates (if included)
* **Target:** Continuous value — Gold Price
* **Type:** Regression problem

## Workflow

### 1. Data Collection

Load historical gold price dataset

### 2. Data Pre-processing

* Handle missing values
* Feature selection
* Data normalization (if needed)

### 3. Exploratory Data Analysis (EDA)

* Correlation analysis
* Visualization of trends and relationships

### 4. Train-Test Split

Split dataset into training and testing sets

### 5. Model Training

Train a **Random Forest Regressor**

### 6. Model Evaluation

Evaluate using metrics such as:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score
In this case, we used  R² Score.


## Random Forest Overview

Random Forest is an **ensemble learning algorithm** that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

1. It builds multiple decision trees using different subsets of the data (bagging).

2. Each tree makes a prediction, and the final output is the **average** of all predictions:

[
\hat{y} = \frac{1}{n} \sum_{i=1}^{n} T_i(x)
]

3. It introduces randomness by:

   * Sampling data points (bootstrap sampling)
   * Selecting random subsets of features for splitting

4. Advantages:

   * Reduces overfitting compared to a single decision tree
   * Handles non-linear relationships well
   * Robust to noise and outliers