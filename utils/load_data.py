from utils import csv


def load_thetas():
    df = csv.load("./thetas.csv")

    theta_0 = csv.dataframe(df, "theta_0")[0]
    theta_1 = csv.dataframe(df, "theta_1")[0]
    return (theta_0, theta_1)


def load_dataset():
    df = csv.load("./learning/data.csv")

    kms = csv.dataframe(df, "km")
    prices = csv.dataframe(df, "price")
    return (kms, prices)
