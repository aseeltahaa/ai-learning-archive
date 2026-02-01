# Sonar Rock vs Mine Classification 

Classifies underwater objects as rocks (R) or mines (M) using sonar signal data and machine learning.

## 📋 Project Overview

**Problem:** Distinguish between underwater rocks and naval mines based on sonar return signals  
**Approach:** Binary classification using machine learning algorithms -> Linear Regression
**Dataset:** Sonar returns bounced off metal cylinder (mines) vs rocks  

## 🎯 Objectives

- Build a reliable classifier for sonar signals
- Understand feature importance in sonar data
- Practice complete ML pipeline from data to model evaluation

## 📊 Dataset

- **Source:** UCI Machine Learning Repository - Connectionist Bench (Sonar, Mines vs. Rocks)
- **Size:** 208 samples, 61 features
- **Features:** 60 sonar signal frequencies (0-1 range)
- **Target:** Binary - 'R' (Rock) or 'M' (Mine)
- **Balance:** 97 rocks, 111 mines (relatively balanced)

## Workflow

### 1. Collect the Sonar Data
### 2. Data Pre-processing
### 3. Train-Test Split
### 4. Logistic Regression Model
### 5. Model Evaluation

## Technologies Used

- **Python 3.11**
- **Pandas** - Data manipulation
- **NumPy** - Numerical operations
- **Scikit-learn** - ML algorithms and preprocessing
- **Jupyter Notebook** - Interactive development