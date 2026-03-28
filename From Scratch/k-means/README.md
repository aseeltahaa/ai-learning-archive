# K-Means Clustering

> K-Means is an **Unsupervised Machine Learning Algorithm**.
> It groups data points into clusters based on similarity, without using labeled data.

---

## The Intuition Behind It

K-Means is based on a simple idea:

> **“Points that are similar should belong to the same group.”**

The algorithm tries to:

* Group nearby points together
* Place a **center (centroid)** in each cluster
* Minimize the distance between points and their assigned centroid

---

## How Distance is Measured

To determine similarity, we use **Euclidean Distance**:

```
d(x, c) = √ Σ (xi - ci)^2
```

Where:

* `x` is a data point
* `c` is a centroid
* Smaller distance means higher similarity

---

## How the Algorithm Works

1. Choose the number of clusters `k`
2. Initialize `k` centroids randomly
3. Assign each data point to the nearest centroid
4. Recompute centroids as the mean of assigned points
5. Repeat steps 3–4 until convergence

---

## What is Convergence?

The algorithm stops when:

* Centroids no longer change significantly
* Or a maximum number of iterations is reached

This means the clusters have stabilized.

---

## Objective of K-Means

K-Means aims to minimize the total distance between points and their cluster centers:

```
Σ Σ ||x - μ||²
```

Where:

* `μ` is the centroid of a cluster
* The goal is to make clusters as compact as possible

---

## Key Idea

Each cluster is represented by its **centroid**, which is:

> The average of all points in that cluster

---

## Pseudocode

```
Initialize k centroids randomly

Repeat until convergence:
    Assign each point to nearest centroid
    Recompute centroids as mean of assigned points

Return cluster assignments
```

---

## Important Notes

* K-Means requires choosing hyperparameter `k` beforehand
* Results depend on initial centroid positions
* Works best when clusters are:

  * Spherical
  * Similar in size