 # Random Forest Classifier

This project contains a simple implementation of the **Random Forest algorithm** built from scratch using **NumPy** and a custom **Decision Tree** implementation.

## Overview

Random Forest is an **ensemble learning algorithm** that improves prediction performance by combining multiple Decision Trees.

Each tree:
1. Trains on a **bootstrap sample** (random sampling with replacement).
2. Learns independently.
3. Makes predictions.

The final prediction is obtained by aggregating predictions from all trees.

---

## Features

- Custom Random Forest implementation
- Bootstrap sampling
- Multiple Decision Trees
- Configurable number of trees
- Configurable tree depth
- Configurable minimum split size
- Optional feature selection

---

## Class: `RandomForest`

### Constructor

```python
RandomForest(
    n_trees=10,
    max_depth=10,
    min_samples_split=2,
    n_features=None
)
```

### Parameters

| Parameter | Description |
|----------|-------------|
| `n_trees` | Number of decision trees |
| `max_depth` | Maximum depth of each tree |
| `min_samples_split` | Minimum samples required to split |
| `n_features` | Number of features considered at each split |

---

## Methods

### `fit(X, y)`

Trains the forest.

#### Parameters

```python
X → Feature matrix
y → Target labels
```

#### Process

For each tree:

- Generate bootstrap sample
- Train a Decision Tree
- Store trained tree

Example:

```python
forest.fit(X_train, y_train)
```

---

### `_bootstrap_sample(X, y)`

Private helper function.

Creates a random sample **with replacement**.

Example:

Original:

```plaintext
[1,2,3,4]
```

Possible sample:

```plaintext
[2,2,4,1]
```

---

### `predict(X)`

Generates predictions from all trees.

Current implementation:

```python
return np.array(predictions).mean(axis=0)
```

This returns the **average prediction across trees**.

Example:

```python
predictions = forest.predict(X_test)
```

---

## Notes

Current implementation aggregates predictions using:

```python
mean(axis=0)
```

For **classification**, majority voting is usually preferred:

```python
from scipy.stats import mode
mode(predictions, axis=0)
```

For **regression**, averaging predictions is correct.