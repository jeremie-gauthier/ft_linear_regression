import argparse
from utils import csv, plot
from utils.Data import Data
from utils.load_data import load_thetas, load_dataset
from utils.normalization import normalize, denormalize
from .src.gradient_descent import gradient_descent
from prediction.src.estimate_price import estimate_price


def _normalize_dataset(kms, prices):
    normalized_kms = map(lambda km: normalize(km, kms), kms)
    normalized_prices = map(lambda price: normalize(price, prices), prices)
    return [Data(x, y) for x, y in zip(normalized_kms, normalized_prices)]


def learning(args):
    initial_thetas = load_thetas()
    kms, prices = load_dataset()
    normalized_plots = _normalize_dataset(kms, prices)

    final_thetas = gradient_descent(
        *initial_thetas, normalized_plots, args.learning, args.iterations,
    )
    csv.write_thetas(final_thetas)

    if args.show:
        plot.dataset(kms, prices)
        price_estimations = [
            denormalize(estimate_price(*final_thetas, data.mileage), prices)
            for data in normalized_plots
        ]
        plot.linear_regression(kms, price_estimations)
        plot.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--learning",
        help="set the learning rate (defaults to 1)",
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
    learning(args)
