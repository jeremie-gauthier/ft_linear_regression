from utils import csv
from utils.load_thetas import load_thetas
from .src.Data import Data
from .src.gradient_descent import gradient_descent


def load_dataset():
    df = csv.load("./learning/data.csv")

    kms = csv.dataframe(df, "km")
    prices = csv.dataframe(df, "price")
    plots = [Data(x, y) for x, y in zip(kms, prices)]
    return plots


if __name__ == "__main__":
    plots = load_dataset()
    initial_thetas = load_thetas()

    final_thetas = gradient_descent(initial_thetas[0], initial_thetas[1], plots)

    csv.write_thetas("./thetas.csv", final_thetas)
