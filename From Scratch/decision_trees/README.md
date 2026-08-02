# Decision Tree (Classification)

## How it works

A decision tree predicts by repeatedly asking yes/no questions about feature values until it reaches a leaf, at which point it returns the majority class of the training samples that landed there.

### Growing the tree

At each node, the algorithm:

1. Checks stopping criteria (max depth reached, node is pure, or too few samples to split) — if met, creates a **leaf** holding the most common label.
2. Otherwise, randomly samples `n_features` candidate features to consider (this is what makes the class reusable as a building block for Random Forest).
3. Searches every candidate feature and every unique value in that feature as a possible threshold, picking the (feature, threshold) pair that maximizes **information gain**.
4. Splits the data into left (`<= threshold`) and right (`> threshold`) subsets and recurses on each.

### Splitting criterion: entropy & information gain

Entropy measures the impurity of a set of labels:

```
H(y) = -Σ p_i * log2(p_i)
```

where `p_i` is the proportion of class `i` in `y`. Entropy is `0` for a pure node and maximized when classes are evenly mixed.

Information gain measures how much a split reduces entropy:

```
IG = H(parent) - [ (n_left/n) * H(left) + (n_right/n) * H(right) ]
```

The split with the highest information gain is chosen at each node.

### Predicting

To classify a new sample, walk from the root: at each internal node, go left if the sample's feature value is `<= threshold`, else go right, until a leaf is reached. Return the leaf's stored value.

## API

```python
tree = DecisionTree(min_samples_split=2, max_depth=100, n_features=None)
tree.fit(X, y)
predictions = tree.predict(X_test)
```

| Parameter          | Description                                                                                   | Default |
|--------------------|-----------------------------------------------------------------------------------------------|---------|
| `min_samples_split`| Minimum samples required at a node to attempt a split                                         | `2`     |
| `max_depth`        | Maximum recursion depth before forcing a leaf                                                 | `100`   |
| `n_features`       | Number of features randomly sampled per split. `None` uses all features (standard CART tree); set lower to use this class inside a Random Forest | `None`  |

**Input format:** `X` is a 2D NumPy array of shape `(n_samples, n_features)`. `y` is a 1D NumPy array of **non-negative integer-encoded labels** (`0, 1, 2, ...`), since entropy is computed via `np.bincount`. Remap labels first if they aren't already in this form, e.g. `np.unique(y, return_inverse=True)`.

## Implementation notes

- **Why `n_features` exists on a single tree:** a plain decision tree should consider all features at every split. The random subsampling here only makes sense once this class is reused as the weak learner inside a Random Forest (each tree in the forest gets a random feature subset to decorrelate trees). For a standalone tree, leave it as `None`.
- **Stopping criteria are intentionally simple** — depth, purity, and minimum samples. There's no pruning step (cost-complexity or otherwise), so on noisy data this tree will overfit at high `max_depth`. That's expected for a from-scratch teaching implementation; production libraries (scikit-learn, XGBoost) add pruning and regularization on top of this same core idea.
- **Threshold search is exhaustive**: every unique value in a feature column is tried as a candidate threshold. This is correct but `O(n log n)` per feature per node — fine for learning/small datasets, but it's the first thing to optimize (e.g. via percentile-based bucketing) if you scale this up.
- **Leaf fallback for unsplittable nodes:** if no candidate split improves on the initial `best_gain = -1` (e.g. every sampled feature is constant within the current subset), the tree now falls back to a leaf instead of crashing on a `None` feature index. This edge case is rare on a single tree but becomes much more common once bootstrapped subsets are introduced in Random Forest — worth keeping in mind when this code gets reused there.

## Complexity

- **Training:** `O(n_samples * n_features * log(n_samples) * depth)` roughly, dominated by sorting/scanning thresholds at each node.
- **Prediction:** `O(depth)` per sample.

## Possible extensions

- Gini impurity as an alternative criterion
- Pruning (pre- or post-)
- Feature importance via accumulated information gain per feature
- Support for categorical (non-numeric) splits