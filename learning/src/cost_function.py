def cost_fn(theta_0, theta_1, plots):
    H0 = lambda x: theta_0 + theta_1 * x

    len_dataset = len(plots)
    diff_squares = map(lambda plot: (H0(plot.get_x()) - plot.get_y()) ** 2, plots)

    cost = sum(diff_squares) / (2 * len_dataset)

    return cost


plots = [(0, 0), (1, 1), (2, 2)]

# x, y
# ----
# 0, 0
# 1, 1
# 2, 2
# 3, 3

# pente : 1-0 / 1-0
# (y1 - y0 / x1 - x0)

# resultat attendu pour cost_fn(0, [0,1,2,3]) = 14/6
# X's are indices and Y's are values
# sum squares = 1^2 + 2^2 + 3^2 = 14
# 2 * len(plots) = 6

# diff_squares ne produit pas le bon resultat
