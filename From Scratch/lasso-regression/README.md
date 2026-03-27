Lasso regression (Least Absolute Shrinkage and Selection Operator) is a type of linear regression that adds a regularization penalty to the model to prevent overfitting and perform automatic feature selection.

## How it works

In ordinary linear regression, you minimize the sum of squared residuals. Lasso adds an extra penalty term:

**Cost = Sum of Squared Residuals + λ × Σ|βᵢ|**

Where:
- **λ (lambda)** is the regularization strength (a tuning parameter)
- **|βᵢ|** is the absolute value of each coefficient (the L1 norm)

## Key properties

**Feature selection** — Unlike Ridge regression (which uses L2/squared penalty), Lasso can shrink coefficients all the way to exactly **zero**, effectively removing irrelevant features from the model. This makes it great when you have many features but suspect only a few matter.

**Sparsity** — The resulting model is "sparse" — it uses only a subset of the input features, making it more interpretable.

**Bias-variance tradeoff** — By penalizing large coefficients, Lasso increases bias slightly but reduces variance, leading to better generalization on unseen data.

## Controlling regularization with λ

| λ value | Effect |
|---|---|
| λ = 0 | Ordinary least squares (no regularization) |
| Small λ | Mild shrinkage, most features kept |
| Large λ | Heavy shrinkage, many features zeroed out |
| λ → ∞ | All coefficients → 0 |

## When to use Lasso

- You have **many features** and want automatic selection of the most important ones
- You suspect the true model is **sparse** (few features actually matter)
- You want an **interpretable** model with fewer variables
- You're doing **high-dimensional** data analysis (e.g., genomics, text)