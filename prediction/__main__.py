from utils import csv
from utils.load_thetas import load_thetas
from .src.estimate_price import estimate_price

if __name__ == "__main__":
    theta_0, theta_1 = load_thetas()

    # catch input error
    mileage = float(input("Kilometrage: "))

    estimation = estimate_price(theta_0, theta_1, mileage)

    print(f"Estimation for {mileage} with t0={theta_0} and t1={theta_1} = {estimation}")
