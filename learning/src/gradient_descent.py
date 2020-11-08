from .cost_function import cost_fn
from .derivative_thetas import derivative_thetas
import sys


def _simultaneous_update(theta_0, theta_1, plots, learning_rate):
    deriv_theta_0, deriv_theta_1 = derivative_thetas(theta_0, theta_1, plots)
    new_theta_0 = theta_0 - (learning_rate * deriv_theta_0)
    new_theta_1 = theta_1 - (learning_rate * deriv_theta_1)
    return (new_theta_0, new_theta_1)


def _precision(plots):
    cost = 1
    prev_cost = 0

    def convergence(theta_0, theta_1):
        nonlocal cost, prev_cost

        cost = cost_fn(theta_0, theta_1, plots)
        if abs(prev_cost - cost) < 0.00000000000001:
            return True
        if abs(cost) > 1000000:
            print(
                "[-] There is a divergence in the results. Decrease the learning rate.",
                file=sys.stderr,
            )
            sys.exit(-1)
        prev_cost = cost
        return False

    return convergence


def gradient_descent(theta_0, theta_1, plots, learning_rate, iterations):
    new_theta_0 = 0
    new_theta_1 = 0
    convergence = _precision(plots)
    for i in range(iterations):
        if convergence(new_theta_0, new_theta_1):
            return (new_theta_0, new_theta_1)

        new_theta_0, new_theta_1 = _simultaneous_update(
            new_theta_0, new_theta_1, plots, learning_rate
        )
    return (new_theta_0, new_theta_1)
