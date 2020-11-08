import argparse
from utils import csv
from utils.load_data import load_thetas, load_dataset
from .src.estimate_price import estimate_price
from utils.normalization import normalize, denormalize


def prediction(args):
    thetas = load_thetas()
    kms, prices = load_dataset()
    norm_mileage = normalize(args.mileage, kms)
    estimation = estimate_price(*thetas, norm_mileage)
    if sum(thetas) != 0:
        estimation = denormalize(estimation, prices)

    print(f"Estimation for {args.mileage} is {round(estimation, 2)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mileage", help="set the mileage to estimate", type=float,
    )

    args = parser.parse_args()
    prediction(args)
