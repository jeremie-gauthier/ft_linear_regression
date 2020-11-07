import argparse
from utils import csv, plot
from utils.Data import Data
from utils.load_thetas import load_thetas
from utils.normalization import normalize, denormalize
from .src.gradient_descent import gradient_descent
from prediction.src.estimate_price import estimate_price


def _load_dataset():
    df = csv.load("./learning/data.csv")

    kms = csv.dataframe(df, "km")
    prices = csv.dataframe(df, "price")
    return (kms, prices)


def _normalize_dataset(kms, prices):
    normalized_kms = map(lambda km: normalize(km, kms), kms)
    normalized_prices = map(lambda price: normalize(price, prices), prices)
    return [Data(x, y) for x, y in zip(normalized_kms, normalized_prices)]


def learning(args):
    initial_thetas = load_thetas()
    kms, prices = _load_dataset()
    normalized_plots = _normalize_dataset(kms, prices)

    final_thetas = gradient_descent(
        *initial_thetas, normalized_plots, args.learning, args.iterations,
    )
    csv.write_thetas("./thetas.csv", final_thetas)

    if args.show:
        # natural_plots = [Data(x, y) for x, y in zip(kms, prices)]
        # plot.dataset(natural_plots)

        X = kms
        # normalized_kms = list(map(lambda km: normalize(km, kms), kms))
        # Y = [(km, estimate_price(*final_thetas, km)) for km in kms]
        normalized_kms = list(map(lambda km: normalize(km, kms), kms))
        normalized_prices = list(map(lambda price: normalize(price, prices), prices))
        print(prices)
        Y2 = [
            (
                km,
                estimate_price(*final_thetas, km),
                denormalize(estimate_price(*final_thetas, km), prices),
            )
            for km in normalized_kms
        ]
        print(*final_thetas)
        for v in Y2:
            print(v)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--learning",
        help="set the learning rate (defaults to 0.001)",
        type=float,
        default=1,
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
    print(args)
    learning(args)
