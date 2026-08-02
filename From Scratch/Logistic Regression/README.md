# Logistic Regression

## What is Logistic Regression and how does it work?

Logistic Regression is a ML algorithm used in binary classification (supervised learning)

It begins with a linear combination of input values:

$z = w^\top x + b$

where w is weight and b is the bias

To convert this linear value into a probability between 0 and 1, the model applies the sigmoid function

$$
\hat{y} = \sigma(z) = \frac{1}{1 + e^{-z}}
$$

This function squashes any input value from negative infinity to positive infinity into a range (0, 1).

The output represents the probability that the given input belongs to the class with label 1.

To make the final classification, a decision boundary (typically 0.5) is used:

- if $\hat{y} \ge 0.5$, the model predicts class 1
- if $\hat{y} < 0.5$, the model predicts class 0

## Loss & Cost Function

Loss Function L refers to the error of 1 individual data point while the Cost Function J refers to the average loss across all training data points.

### MSE

In linear regression, MSE works well because it creates a convex "U-shaped" curve with a single global minimum. However, if you use MSE for logistic regression, the resulting error surface will have **multiple local minima**.

### Binary Cross-Entropy / Log Loss

#### Likelihood

Assuming independent training examples, the likelihood of parameters $\theta$ is:

$$
L(\theta) = \prod_{i=1}^{m} \big(h_{\theta}(x^{(i)})\big)^{y^{(i)}}\,\big(1 - h_{\theta}(x^{(i)})\big)^{(1-y^{(i)})}
$$

Where:

- $h_{\theta}(x) = \sigma(\theta^T x) = \frac{1}{1 + e^{-\theta^T x}}$ (sigmoid)
- $y^{(i)} \in \{0,1\}$ is the label for example $i$
- $m$ is the number of training examples

$$
\ell(\theta) = \sum_{i=1}^{m} \Big[ y^{(i)}\log\big(h_{\theta}(x^{(i)})\big) + (1-y^{(i)})\log\big(1-h_{\theta}(x^{(i)})\big) \Big]
$$

#### Cost function :

$$
J(\theta) = -\frac{1}{m}\,\ell(\theta)
$$

## Gradient Descent

Our goal is to minimize the cost function. To reach the minimum, we iteratively update the weights (parameters) by moving in the opposite direction of the gradient:

$$
\theta_j := \theta_j - \alpha \frac{\partial J(\theta)}{\partial \theta_j} \quad \text{for } j = 0,1,\ldots,n
$$

Where:

- $\theta_j$ is the parameter (weight or bias)
- $\alpha$ is the learning rate
- $J(\theta)$ is the **cost function** for logistic regression given by:

$$
J(\theta) = - \frac{1}{m} \sum_{i=1}^{m} \Big[ y^{(i)} \log h_\theta(x^{(i)}) + (1 - y^{(i)}) \log (1 - h_\theta(x^{(i)})) \Big]
$$

The **gradients** are computed as:

$$
\frac{\partial J(\theta)}{\partial \theta_j} = \frac{1}{m} \sum_{i=1}^{m} \big(h_\theta(x^{(i)}) - y^{(i)}\big)\,x_j^{(i)}
$$

Then, for **each iteration**, update all parameters simultaneously:

$$
\theta_j := \theta_j - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} \big(h_\theta(x^{(i)}) - y^{(i)}\big)\,x_j^{(i)}
$$