# From Scratch

> Building AI algorithms from the ground up — no shortcuts, no black boxes.  
> Each implementation includes a breakdown of the theory, pseudocode, and the algorithm applied to a real dataset.

---

## What is a ML Model?

A ML Model is a function that tries to find the relationship between the features and the target variable. It tries to find patterns in data, understand the data and trains on the data.
Based on this learning, the model makes predictions and recognizes patterns.

---

## Types of Learning

### Supervised Learning

In Supervised Learning, the algorithm learns from labelled data. It has two types:

#### Classification:

It predicts a class or discrete values.
Some examples include: Logistic Regression, K-Nearest Neighbors, etc.

#### Regression:

It predicts a continuous numerical value.
Some examples include: Linear Regression, Polynomial Regression, etc.


### Unsupervised Learning

In Unsupervised Learning, the algorithm learns from **unlabelled data**. There is no target variable — the model tries to find hidden structure or patterns on its own. It has two main types:

#### Clustering:
Groups similar data points together without being told what the groups are.
Some examples include: K-Means, DBSCAN, Hierarchical Clustering.

#### Dimensionality Reduction:
Reduces the number of features while preserving the most important information.
Some examples include: PCA (Principal Component Analysis), t-SNE.


### Reinforcement Learning

In Reinforcement Learning, an **agent** learns by interacting with an **environment**. It takes actions, receives **rewards** or **penalties**, and learns to maximize its cumulative reward over time. There is no labelled dataset — the model learns from experience.
Some examples include: Q-Learning, Deep Q-Networks (DQN).

---

## How to Choose the Right Model?

Model selection involves choosing the best-suited model for a particular problem. Selecting a model depends on multiple factors:

1. **Type of data available:**
   - Images and Videos → CNN
   - Text / Speech → RNN
   - Numerical Data → SVM, Logistic Regression, Decision Trees, etc.

2. **The task:**
   - Classification
   - Regression
   - Clustering
   - Association

3. **Size of the dataset:**
   - Small dataset → simpler models (Linear Regression, KNN) to avoid overfitting
   - Large dataset → complex models (Neural Networks, SVMs with kernels)

4. **Interpretability requirements:**
   - Need to explain predictions → Decision Trees, Linear Regression
   - Performance is priority → Neural Networks, Ensemble methods

---

## Model Performance

### Overfitting:
It happens when the model learns the details and noise in the training dataset instead of the general pattern.

#### Sign:
Model performs well on the training data but poorly on the testing data.

#### Causes:
- Less data
- Increased complexity of the model
- Unnecessary number of layers in a neural network

#### Preventing Overfitting:
- Collect more data
- Reduce the number of layers in a neural network
- Early stopping
- Bias-Variance Tradeoff
- Use Dropouts
- Regularization (L1 / L2)


### Underfitting:
It happens when the model is too simple to capture the underlying pattern in the data.

#### Sign:
Model performs poorly on both the training data and the testing data.

#### Causes:
- Model is too simple for the complexity of the data
- Too few features (important information is missing)
- Too little training time

#### Preventing Underfitting:
- Use a more complex model
- Add more relevant features
- Train for longer
- Reduce regularization if it is too aggressive

---

## Bias-Variance Tradeoff

- **Bias:** Error from wrong assumptions in the model. A high-bias model is too simple and misses the real pattern.
- **Variance:** Error from sensitivity to small fluctuations in the training data. A high-variance model learns the noise instead of the signal.

| | Bias | Variance |
|---|---|---|
| Underfitting | High | Low |
| Overfitting | Low | High |
| Ideal | Low | Low |

#### Techniques to Achieve a Better Bias-Variance Tradeoff:
- **Cross-validation** — evaluate the model on multiple splits to get a reliable estimate of performance
- **Regularization (L1/L2)** — penalizes model complexity to reduce variance
- **Ensemble methods** — combine multiple models (e.g. bagging reduces variance, boosting reduces bias)
- **Increase training data** — helps reduce variance without increasing bias
- **Feature selection** — removing irrelevant features reduces variance

---

## Loss Function

A loss function measures **how wrong the model's predictions are**. The goal of training is to minimize this value.

| Task | Common Loss Functions |
|---|---|
| Regression | Mean Squared Error (MSE), Mean Absolute Error (MAE) |
| Binary Classification | Binary Cross-Entropy |
| Multi-class Classification | Categorical Cross-Entropy |

**Example — MSE:**
```
Loss = (1/n) * Σ(y_actual - y_predicted)²
```
The larger the error, the higher the loss. The model adjusts its parameters to bring this value as close to 0 as possible.

---

## Model Evaluation

How do we know if our model is actually good? We use evaluation metrics.

| Task | Metric | What it measures |
|---|---|---|
| Regression | R² Score | How much variance in the target the model explains |
| Regression | MAE / MSE / RMSE | Average prediction error |
| Classification | Accuracy | % of correct predictions |
| Classification | Precision | Of all predicted positives, how many were actually positive |
| Classification | Recall | Of all actual positives, how many did the model catch |
| Classification | F1-Score | Harmonic mean of Precision and Recall |

**Important:** Always evaluate on a **held-out test set** that the model has never seen during training.

---

## Model Parameters vs Hyperparameters

| | Parameters | Hyperparameters |
|---|---|---|
| **What they are** | Internal values the model learns from data | External settings you define before training |
| **Who sets them** | The model (during training) | You (before training) |
| **Examples** | Weights, biases | Learning rate, number of layers, k in KNN |
| **How to tune** | Automatically via optimization | Manually or via Grid Search / Random Search |

---

## Model Optimization using Gradient Descent
Gradient Descent is an optimization algorithm for finding the **local minimum** of a differentiable function.

### Outline:
1. Start with some random values of a and b.
2. Keep changing them to reduce the loss function until we settle at or near a minimum.
Note: The function may have more than one minimum; it does not have to be a parabola. We reach a local minimum according to our intial values of a and b.

### Update Rules:
We repeat the following until the values of a and b converge:
**(Simulataneously updated)**
a = a - α d/da J(a,b)
b = b - α d/db J(a, b)

#### Learning Rate α
- Its value is between [0,1]
- It controls how big the step is per iteration
- If it is too small, the algorithm shows a slow performace
- It if is too large, the algorithm may fail to converge as it overshoots

#### Derivative d/da J(a,b)
d/da J(a, b) descrives the slope of the tangent at a specific point
- If it is positive, the function is inceasing
- If it is negative, the function is decreasing
- If it is zero, we have reached a minimum

#### Variants:

| Variant | How it works | When to use |
|---|---|---|
| Batch Gradient Descent | Uses the entire dataset per update | Small datasets |
| Stochastic Gradient Descent (SGD) | Uses one sample per update | Large datasets |
| Mini-batch Gradient Descent | Uses a small batch per update | Most common in practice |

#### Learning Rate:
- Too high → overshoots the minimum, loss may diverge
- Too low → very slow convergence
- Just right → converges smoothly to the minimum

---

## Algorithms

| Algorithm | Folder | Description |
|---|---|---|
| Linear Regression | [`linear-regression/`](./linear-regression/) | Predict continuous values by fitting a line through data using gradient descent |
| Logistic Regression | [`logistic-regression/`](./logistic-regression/) | Binary classification using the sigmoid function and log loss |
| Support Vector Machine | [`svm/`](./svm/) | Find the optimal hyperplane that maximizes the margin between classes |
| K-Nearest Neighbors | [`knn/`](./knn/) | Classify points based on the majority vote of their k closest neighbors |