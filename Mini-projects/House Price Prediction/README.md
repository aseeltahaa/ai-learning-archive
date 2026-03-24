# California Housing Price Prediction

Predicts housing prices in California districts using machine learning and gradient boosting.

## Project Overview

**Problem:** Predict median house values based on district-level features in California
**Approach:** Regression using machine learning algorithms → XGBoost Regressor
**Dataset:** California Housing dataset (based on 1990 U.S. Census data)

## Objectives

* Build an accurate regression model for house price prediction
* Understand the impact of different features on housing prices
* Practice a complete ML pipeline from data preprocessing to model evaluation

## Dataset

* **Source:** California Housing Dataset (Scikit-learn)
* **Size:** 20,640 samples, 8 features
* **Features:**

  * MedInc (Median Income)
  * HouseAge
  * AveRooms
  * AveBedrms
  * Population
  * AveOccup
  * Latitude
  * Longitude
* **Target:** Median House Value (continuous numerical value)
* **Balance:** Continuous distribution (regression problem)

## Workflow

### 1. Load the California Housing Data

### 2. Data Pre-processing

### 3. Exploratory Data Analysis (EDA)

### 4. Train-Test Split

### 5. XGBoost Regression Model

### 6. Model Evaluation

## Technologies Used

* **Python 3.11**
* **Pandas** - Data manipulation
* **NumPy** - Numerical operations
* **Matplotlib / Seaborn** - Data visualization
* **Scikit-learn** - Preprocessing and evaluation metrics
* **XGBoost** - Gradient boosting model
* **Jupyter Notebook** - Interactive development

# XGBoost Overview

XGBoost (Extreme Gradient Boosting) is a powerful and efficient machine learning algorithm used for supervised learning tasks like regression and classification.

1. It builds models using **decision trees** in a sequential manner.
2. Each new tree tries to **correct the errors** made by previous trees.
3. It uses **gradient descent optimization** to minimize the loss function.
4. XGBoost includes **regularization** to prevent overfitting and improve generalization.

### Key Advantages:

* High performance and speed
* Handles missing values effectively
* Built-in regularization (L1 & L2)
* Works well with structured/tabular data
