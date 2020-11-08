import matplotlib.pyplot as plt


def dataset(kms, prices):
    plt.title("Prices evolution through mileage")
    plt.ylabel("Prices")
    plt.xlabel("Mileage")
    dataset = plt.plot(kms, prices, "ro")
    plt.setp(dataset, color="cornflowerblue")


def linear_regression(kms, prices):
    line = plt.plot(kms, prices)
    plt.setp(line, color="red")


def show():
    plt.show()
