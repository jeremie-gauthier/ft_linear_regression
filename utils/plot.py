import matplotlib.pyplot as plt


def dataset(kms, prices):
    plt.ylabel("prices")
    plt.xlabel("mileage")
    dataset = plt.plot(kms, prices, "ro")
    plt.setp(dataset, color="cornflowerblue")


def update_lin_reg(line, *coords):
    line.set_ydata(*coords)


def create_lin_reg(kms, prices):
    linear_regression = plt.plot(kms, prices)
    plt.setp(linear_regression, color="red")
    return linear_regression


def show():
    plt.show()
