import pandas as pd
import matplotlib.pyplot as plt


# Load dataset
data = pd.read_csv("data.csv")


# Mean Squared Error
def loss_function(m, b, points):
    total_error = 0

    for i in range(len(points)):
        x = points.iloc[i].study_hours
        y = points.iloc[i].score

        total_error += (y - (m * x + b)) ** 2

    return total_error / float(len(points))


# Compute gradients and update parameters
def gradient_descent(m_current, b_current, points, learning_rate):
    m_gradient = 0
    b_gradient = 0

    N = float(len(points))

    for i in range(len(points)):
        x = points.iloc[i].study_hours
        y = points.iloc[i].score

        error = y - (m_current * x + b_current)

        m_gradient += -(2 / N) * x * error
        b_gradient += -(2 / N) * error

    new_m = m_current - learning_rate * m_gradient
    new_b = b_current - learning_rate * b_gradient

    return new_m, new_b


# Training loop
def linear_regression(points, starting_m, starting_b,
                      learning_rate, num_iterations):

    m = starting_m
    b = starting_b

    for epoch in range(num_iterations):

        m, b = gradient_descent(
            m,
            b,
            points,
            learning_rate
        )

        if epoch % 10 == 0:
            loss = loss_function(m, b, points)
            print(
                f"Epoch {epoch:3d} | "
                f"Loss: {loss:.2f} | "
                f"m={m:.3f} | "
                f"b={b:.3f}"
            )

    return m, b


# Hyperparameters
m = 0
b = 0
learning_rate = 0.002
epochs = 1000


# Train model
m, b = linear_regression(
    data,
    m,
    b,
    learning_rate,
    epochs
)

print("\nFinal Parameters")
print(f"Slope (m): {m:.4f}")
print(f"Intercept (b): {b:.4f}")


# Plot
plt.scatter(
    data["study_hours"],
    data["score"]
)

x = data["study_hours"]
y_pred = m * x + b

plt.plot(
    x,
    y_pred
)

plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.title("Linear Regression From Scratch")

plt.show()