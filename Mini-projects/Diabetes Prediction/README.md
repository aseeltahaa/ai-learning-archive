# Diabetes Prediction

Predicts whether a patient is diabetic or non-diabetic using clinical health data and machine learning.

## Project Overview

**Problem:** Classify patients as diabetic or non-diabetic based on diagnostic health measurements  
**Approach:** Binary classification using machine learning algorithms → Support Vector Machine (SVM)  
**Dataset:** Pima Indians Diabetes Database — clinical measurements from female patients of Pima Indian heritage  

## Objectives

- Build a reliable classifier for diabetes prediction from medical data
- Understand feature importance in clinical diagnostic data
- Practice a complete ML pipeline from data ingestion to model evaluation

## Dataset

- **Source:** UCI Machine Learning Repository / Kaggle — Pima Indians Diabetes Database
- **Size:** 768 samples, 9 features
- **Features:** 8 clinical measurements (e.g., glucose level, BMI, blood pressure, insulin)
- **Target:** Binary — `0` (Non-Diabetic) or `1` (Diabetic)
- **Balance:** 500 non-diabetic, 268 diabetic (moderately imbalanced)

## Workflow

### 1. Collect the Diabetes Data
### 2. Data Pre-processing
### 3. Train-Test Split
### 4. SVM Model Training
### 5. Model Evaluation

## SVM Overview

Support Vector Machine (SVM) is a powerful supervised learning model used for binary classification.

1. It maps input features (like glucose level, BMI, etc.) into a **high-dimensional feature space**.

2. The algorithm finds the **optimal hyperplane** that best separates the two classes by maximizing the **margin** — the distance between the hyperplane and the nearest data points (called **support vectors**):

$$
f(x) = \mathbf{w}^T \mathbf{x} + b
$$

3. For non-linearly separable data, SVM uses a **kernel function** to transform the input space:

   - **Linear Kernel** — works well for linearly separable data  
   - **RBF (Radial Basis Function) Kernel** — maps data into a higher-dimensional space to handle non-linear boundaries  

4. The model then applies a **decision rule**:

   - If $f(x) \geq 0$ → class `1` (Diabetic)  
   - If $f(x) < 0$ → class `0` (Non-Diabetic)