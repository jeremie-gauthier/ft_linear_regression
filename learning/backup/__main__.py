from pandas import read_csv
from math import isnan, isinf


def cost(theta_0, theta_1, x, y):
    return theta_0 + (theta_1 * x) - y


def partial_derivatives(theta_0, theta_1):
    global X, Y

    derivative_theta_0 = 0.0
    derivative_theta_1 = 0.0
    M = len(X)

    for i in range(0, len(X)):
        var_cost = cost(theta_0, theta_1, X[i], Y[i])
        derivative_theta_0 += var_cost
        derivative_theta_1 += var_cost * X[i]

    derivative_theta_0 = (1 / M) * derivative_theta_0
    derivative_theta_1 = (1 / M) * derivative_theta_1
    return (derivative_theta_0, derivative_theta_1)


def update_thetas(theta_0, theta_1):
    global X, Y, learning_rate

    (derivative_theta_0, derivative_theta_1) = partial_derivatives(theta_0, theta_1)
    new_theta_0 = theta_0 - (learning_rate * derivative_theta_0)
    new_theta_1 = theta_1 - (learning_rate * derivative_theta_1)
    return (new_theta_0, new_theta_1)


def gradient_descent(initial_theta_0, initial_theta_1, iterations):
    tmp_theta_0 = initial_theta_0
    tmp_theta_1 = initial_theta_1

    for i in range(iterations):
        (new_theta_0, new_theta_1) = update_thetas(tmp_theta_0, tmp_theta_1)
        if (
            isnan(new_theta_0)
            or isnan(new_theta_1)
            or isinf(new_theta_0)
            or isinf(new_theta_1)
        ):
            continue
        tmp_theta_0 = new_theta_0
        tmp_theta_1 = new_theta_1

    return (tmp_theta_0, tmp_theta_1)


if __name__ == "__main__":
    dataset = read_csv("./learning/data.csv")
    dataset = dataset.dropna()
    X = dataset.iloc[0 : len(dataset), 0]
    Y = dataset.iloc[0 : len(dataset), 1]

    learning_rate = 0.01

    (final_theta_0, final_theta_1) = gradient_descent(0.0, 0.0, 2000)
    print(
        f"After {2000} iterations theta_0 = {final_theta_0}, theta_1 = {final_theta_1}"
    )
