import numpy as np

class LassoRegression:
    """
    Attributes:
    learning_rate   : Step size used during gradient descent updates.
    number_of_iterations : Number of iterations for the gradient descent optimization.
    lambda_param    : Regularization strength (controls L1 penalty).
    w               : Weight vector for the features.
    b               : Bias (intercept) term.
    m               : Number of training samples.
    n               : Number of features.
    """

    def __init__(self, learning_rate, number_of_iterations, lambda_param=0.01):
        self.learning_rate = learning_rate
        self.number_of_iterations = number_of_iterations
        self.lambda_param = lambda_param

    def fit(self, X, Y):
        self.m, self.n = X.shape
        self.w = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.Y = Y

        for _ in range(self.number_of_iterations):
            self.update_weights()

    def update_weights(self):
        Y_prediction = self.predict(self.X)

        # Compute gradients (same as Linear Regression)
        dw = -(2 / self.m) * self.X.T.dot(self.Y - Y_prediction)
        db = -(2 / self.m) * np.sum(self.Y - Y_prediction)

        # Add L1 penalty: subgradient of λ * Σ|wᵢ| = λ * sign(wᵢ)
        dw += self.lambda_param * np.sign(self.w)

        self.w = self.w - self.learning_rate * dw
        self.b = self.b - self.learning_rate * db

    def predict(self, X):
        return X.dot(self.w) + self.b