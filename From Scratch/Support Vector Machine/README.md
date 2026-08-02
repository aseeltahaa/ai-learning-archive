# Support Vector Machine (SVM)

## Idea

Support Vector Machines (SVMs) use a linear model to find a **decision boundary (hyperplane)** that best separates the data.

The best hyperplane is the one that:

> **Maximizes the margin (distance) between the closest points of the two classes.**

These closest points are called **support vectors**.

---

## Linear Decision Function

We define:

$$f(x) = w \cdot x - b$$

where:

- $w$ → weight vector (controls orientation of hyperplane)
- $b$ → bias (shifts hyperplane)

---

## Classification Constraints (Hard Margin)

For correct classification:

### Positive class ($y_i = +1$)

$$w \cdot x_i - b \geq 1$$

### Negative class ($y_i = -1$)

$$w \cdot x_i - b \leq -1$$

### Unified form

$$y_i (w \cdot x_i - b) \geq 1$$

where:

$$y_i \in \{-1, +1\}$$

---

## Hinge Loss

SVM uses **hinge loss** to penalize misclassification or low-margin points:

$$L_i = \max(0, 1 - y_i (w \cdot x_i - b))$$

Interpretation:

- If $y_i f(x_i) \geq 1$ → no loss
- If $y_i f(x_i) < 1$ → loss increases linearly

---

## Objective Function (with Regularization)

$$J = \lambda \|w\|^2 + \frac{1}{n} \sum_{i=1}^{n} \max(0, 1 - y_i (w \cdot x_i - b))$$

### Components:

- $\lambda \|w\|^2$ → regularization (maximizes margin)
- Hinge loss → penalizes misclassification / margin violations

---

## Per-sample Loss Behavior

### Case 1: Correct and confident ($y_i f(x_i) \geq 1$)

$$J_i = \lambda \|w\|^2$$

### Case 2: Inside margin or misclassified ($y_i f(x_i) < 1$)

$$J_i = \lambda \|w\|^2 + 1 - y_i (w \cdot x_i - b)$$

---

## Gradients

### If $y_i f(x_i) \geq 1$:

$$\frac{\partial J_i}{\partial w} = 2\lambda w$$

$$\frac{\partial J_i}{\partial b} = 0$$

### If $y_i f(x_i) < 1$:

$$\frac{\partial J_i}{\partial w} = 2\lambda w - y_i x_i$$

$$\frac{\partial J_i}{\partial b} = -y_i$$

---

## Update Rules (Gradient Descent)

Let learning rate = $\alpha$

### Case 1: $y_i f(x_i) \geq 1$

$$w = w - \alpha (2\lambda w)$$

$$b = b$$

### Case 2: $y_i f(x_i) < 1$

$$w = w - \alpha (2\lambda w - y_i x_i)$$

$$b = b + \alpha y_i$$

---

## Training Steps

1. Initialize weights $w$ and bias $b$
2. Convert labels to $\{-1, +1\}$
3. For several iterations:
   - Pick training samples
   - Apply update rules based on condition
4. Repeat until convergence

---

## Prediction

For a new input $x$:

$$\hat{y} = \text{sign}(w \cdot x - b)$$

- If result $\geq 0$ → class $+1$
- If result $< 0$ → class $-1$

---

## Key Insight

SVM does two things at once:

- Minimizes classification error (hinge loss)
- Maximizes margin (via $\|w\|^2$)

> The result is a decision boundary that is both **accurate and maximally confident**.