from .cost_function import cost_fn
from prediction.src.estimate_price import estimate_price


def derivative_theta_0(theta_0, theta_1, plots):
    return sum(
        map(
            lambda plot: estimate_price(theta_0, theta_1, plot.mileage) - plot.price,
            plots,
        )
    ) / len(plots)


def derivative_theta_1(theta_0, theta_1, plots):
    return sum(
        map(
            lambda plot: (estimate_price(theta_0, theta_1, plot.mileage) - plot.price)
            * plot.mileage,
            plots,
        )
    ) / len(plots)


def simultaneous_update(theta_0, theta_1, plots, learning_rate):
    new_theta_0 = learning_rate * derivative_theta_0(theta_0, theta_1, plots)
    new_theta_1 = learning_rate * derivative_theta_1(theta_0, theta_1, plots)
    return (new_theta_0, new_theta_1)


def gradient_descent(theta_0, theta_1, plots, learning_rate=0.01, iterations=100):
    new_theta_0 = theta_0
    new_theta_1 = theta_1
    for i in range(iterations):
        new_theta_0, new_theta_1 = simultaneous_update(
            new_theta_0, new_theta_1, plots, learning_rate
        )

    return (new_theta_0, new_theta_1)
