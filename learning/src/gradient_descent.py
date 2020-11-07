from .cost_function import cost_fn
from .derivative_thetas import derivative_thetas


def _simultaneous_update(theta_0, theta_1, plots, learning_rate):
    deriv_theta_0, deriv_theta_1 = derivative_thetas(theta_0, theta_1, plots)
    new_theta_0 = theta_0 - (learning_rate * deriv_theta_0)
    new_theta_1 = theta_1 - (learning_rate * deriv_theta_1)
    return (new_theta_0, new_theta_1)


def gradient_descent(theta_0, theta_1, plots, learning_rate, iterations):
    new_theta_0 = 0
    new_theta_1 = 0
    for i in range(iterations):
        new_theta_0, new_theta_1 = _simultaneous_update(
            new_theta_0, new_theta_1, plots, learning_rate
        )
    return (new_theta_0, new_theta_1)
