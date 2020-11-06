from prediction.src.estimate_price import estimate_price


def _base_derivation(theta_0, theta_1, plot):
    return estimate_price(theta_0, theta_1, plot.mileage) - plot.price


def _extended_derivation(theta_0, theta_1, plot):
    return _base_derivation(theta_0, theta_1, plot) * plot.mileage


def derivative_thetas(theta_0, theta_1, plots):
    M = len(plots)

    derivee_theta_0 = (
        sum(map(lambda plot: _base_derivation(theta_0, theta_1, plot), plots)) / M
    )
    derivee_theta_1 = (
        sum(map(lambda plot: _extended_derivation(theta_0, theta_1, plot), plots)) / M
    )

    return (derivee_theta_0, derivee_theta_1)
