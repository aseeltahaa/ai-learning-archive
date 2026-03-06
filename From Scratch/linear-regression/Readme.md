Got it — you want **exactly the same Markdown style** (with `##`, `>`, code blocks, etc.) and **no LaTeX**, just readable math like you originally wrote. I kept your formatting and only improved the **math explanation and gradient section**.

---

# Linear Regression

> Linear Regression is a Supervised Machine Learning Algorithm.
> It finds a linear relationship between the input features and the output by fitting a straight line through the data.

---

## The Math Behind It

The general equation of a straight line is given by:

```
y = a*x + b
```

Where:

1. **a (weight)** is the slope:
   The slope defines how steep the line is.
   Increasing it makes the line steeper (the output increases more rapidly with each unit increase in x).

2. **b (bias)** is the y-intercept:
   It defines the intersection of the line with the y-axis (value of the prediction when x is zero).
   Increasing it shifts the line upwards.

---

## What if We Have More Than One Feature?

> Multiple Linear Regression

It is an extension of linear regression that uses two or more input features.

The general equation is given by:

```
y = b + a1*x1 + a2*x2 + ... + an*xn
```

Each feature `xi` has its own weight `ai` that controls how much that feature contributes to the prediction.

---

## Advantages

1. Very simple to implement and interpret
2. Performs well on data with a linear relationship
3. Computationally efficient — scales well to large datasets
4. Weights give direct insight into feature importance

---

## Disadvantages

1. Not suited for data with non-linear relationships
2. Prone to underfitting on complex data
3. Sensitive to outliers — a single extreme value can pull the line significantly
4. Assumes features are independent (multicollinearity can distort the weights)

---

## Model Evaluation: Loss Function

> The loss function measures how far the predicted values are from the true values.
> The goal of training is to **minimize this value**.

For Linear Regression, we use **Mean Squared Error (MSE)**:

```
Loss = (1/n) * Σ (yi - ŷi)^2
```

Where:

* `n` = number of data points
* `yi` = actual value
* `ŷi` = predicted value

Squaring the errors ensures that:

* Positive and negative errors don't cancel each other out
* Larger errors are penalized more heavily

---

## How to Find the Optimal Model?

> We need to find the values of `a` (weight) and `b` (bias) that minimize the loss function.

### Gradient Descent

Gradient Descent is an optimization algorithm that iteratively updates the model's parameters to minimize the loss function.

> **Intuition:**
> Think of the loss function as a valley. Gradient Descent starts at a random point and takes small steps downhill in the direction of steepest descent until it reaches the lowest point (minimum loss).

---

## Parameter Update Rule

At each iteration, the parameters are updated using:

```
a = a - α * ∂Loss/∂a
b = b - α * ∂Loss/∂b
```

Where:

* `α` (alpha) is the **learning rate** — controls the size of each step
* `∂Loss/∂a` and `∂Loss/∂b` are the **gradients** — the derivatives of the loss function with respect to each parameter

---

## Computing the Gradients

The gradients are obtained by taking the derivative of the **Mean Squared Error** loss function.

```
Loss = (1/n) * Σ (yi - ŷi)^2
```

Where the prediction is:

```
ŷi = a*xi + b
```

Taking the derivative of the loss with respect to the parameters gives:

```
∂Loss/∂a = (-2/n) * Σ xi * (yi - ŷi)
```

```
∂Loss/∂b = (-2/n) * Σ (yi - ŷi)
```

These gradients tell us **how much the loss changes when we adjust the parameters**.

---

## The Learning Rate

The learning rate `α` is a hyperparameter that controls how big each update step is.

| Learning Rate | Effect                                       |
| ------------- | -------------------------------------------- |
| Too high      | Overshoots the minimum — loss may diverge    |
| Too low       | Very slow convergence — takes too many steps |
| Just right    | Converges smoothly and efficiently           |

---

## Gradient Descent Variants

| Variant          | Uses                      | Pro                | Con                        |
| ---------------- | ------------------------- | ------------------ | -------------------------- |
| Batch            | Entire dataset per update | Stable convergence | Slow on large data         |
| Stochastic (SGD) | One sample per update     | Fast updates       | Noisy, less stable         |
| Mini-batch       | Small batch per update    | Balance of both    | Requires tuning batch size |

---

## Pseudocode

```
Initialize a = 0, b = 0
Set learning rate α and number of iterations

For each iteration:
    Compute predictions: ŷ = a*X + b
    Compute loss: MSE = (1/n) * Σ(y - ŷ)^2
    Compute gradients:
        da = (-2/n) * Σ X * (y - ŷ)
        db = (-2/n) * Σ (y - ŷ)
    Update parameters:
        a = a - α * da
        b = b - α * db

Return a, b
```

---

## When to Use Linear Regression?

* The relationship between features and target is approximately linear
* You need an interpretable and explainable model
* You are working with continuous numerical output
* You want a quick baseline model before trying more complex approaches