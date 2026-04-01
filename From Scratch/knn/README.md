# K-Nearest Neighbors (KNN)

> K-Nearest Neighbors is a **Supervised Machine Learning Algorithm**.
> It classifies a data point based on the labels of its closest neighbors in the feature space.

---

## The Intuition Behind It

KNN works on a simple idea:

> **“Similar points exist close to each other.”**

When a new data point arrives:

* We look at the **k closest points**
* Assign the label based on **majority voting**

---

## How Distance is Measured

To determine how close points are, we use **Euclidean Distance**:

```
d(p, q) = √ Σ (pi - qi)^2
```

Where:

* `p` and `q` are two data points
* The smaller the distance, the more similar the points

---

## How the Algorithm Works

1. Choose the number of neighbors `k`
2. Compute distance from the new point to all training points
3. Sort distances in ascending order
4. Select the top `k` nearest neighbors
5. Perform **majority voting** to assign the class

--

## When to Use KNN?

* Data is **small to medium sized**
* Decision boundary is **non-linear**
* You want a **simple baseline model**
* No need for training time

---

## Pseudocode

```
Store all training data

For each new point:
    Compute distance to all points
    Sort distances
    Select top k neighbors
    Count labels
    Return most common label
```

---

# Choosing Hyperparameter K:

There is no fixed rule for choosing K. The best value depends on the dataset and how the accuracy curve behaves. That is why testing multiple values of K is necessary instead of choosing one blindly.

- **Prefer stability over single high accuracy**
    
    Choose a value of K where performance is **consistent**, not just where accuracy briefly peaks.
    
- **Small K → Overfitting**
    - Highly sensitive to noise and outliers
    - Relies too much on individual data points
    - Leads to unstable predictions
- **Large K → Underfitting**
    - Over-smooths the data
    - Ignores local patterns
    - Becomes biased toward the majority class
- **Increasing K doesn’t always improve performance**
    
    After a certain point, performance can **decrease** as the model becomes too simple.
    
- **If multiple K values perform similarly**
    
    Prefer the **larger K**, since it is more robust and less sensitive to noise.