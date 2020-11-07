from utils import csv
from utils.load_thetas import load_thetas
from utils.normalization import normalize
from .src.Data import Data
from .src.gradient_descent import gradient_descent
import argparse


def _load_dataset():
    df = csv.load("./learning/data.csv")

    kms = csv.dataframe(df, "km")
    prices = csv.dataframe(df, "price")
    return (kms, prices)


def _normalize_dataset(kms, prices):
    return [Data(x, y) for x, y in zip(normalize(kms), normalize(prices))]


def learning(args):
    initial_thetas = load_thetas()
    kms, prices = _load_dataset()
    plots = _normalize_dataset(kms, prices)

    final_thetas = gradient_descent(
        initial_thetas[0], initial_thetas[1], plots, args.learning, args.iterations
    )
    csv.write_thetas("./thetas.csv", final_thetas)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--learning",
        help="set the learning rate (defaults to 0.001)",
        type=float,
        default=0.001,
    )
    parser.add_argument(
        "-i",
        "--iterations",
        help="set the number of iterations (defaults to 1000)",
        type=int,
        default=1000,
    )
    parser.add_argument(
        "-s",
        "--show",
        help="show the dataset with liner regression",
        action="store_true",
    )

    args = parser.parse_args()
    learning(args)
