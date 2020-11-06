from utils import csv
from utils.load_thetas import load_thetas
from utils.normalization import normalize
from .src.Data import Data
from .src.gradient_descent import gradient_descent


def load_dataset():
    df = csv.load("./learning/data.csv")

    kms = csv.dataframe(df, "km")
    prices = csv.dataframe(df, "price")
    return (kms, prices)


def normalize_dataset(kms, prices):
    return [Data(x, y) for x, y in zip(normalize(kms), normalize(prices))]


if __name__ == "__main__":
    initial_thetas = load_thetas()
    kms, prices = load_dataset()
    plots = normalize_dataset(kms, prices)

    final_thetas = gradient_descent(initial_thetas[0], initial_thetas[1], plots)
    csv.write_thetas("./thetas.csv", final_thetas)
