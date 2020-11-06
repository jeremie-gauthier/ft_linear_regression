def cost_fn(theta_0, theta_1, plots):
    H0 = lambda plotX: theta_0 + (theta_1 * plotX)

    len_dataset = len(plots)
    diff_squares = map(lambda plot: (H0(plot.x) - plot.y) ** 2, plots)

    cost = sum(diff_squares) / (2 * len_dataset)

    return cost


plots = [(0, 0), (1, 1), (2, 2)]
