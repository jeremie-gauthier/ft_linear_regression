import pandas as pd


def estimatePrice(mileage, theta_0, theta_1):
    return theta_0 + theta_1 * mileage


def cost(mileage, price, M, extend_predicate=False):
    for i in range(M):
        if extend_predicate:
            yield (estimatePrice(mileage[i], 0, 0) - price[i]) * mileage[i]
        else:
            yield estimatePrice(mileage[i], 0, 0) - price[i]


def linearRegression(mileage, price, M, learningRate=0.001):
    tmpTheta_0 = 0.0
    tmpTheta_1 = 0.0
    M = len(mileage)

    # for i in range(M):
    tmpTheta_0 = learningRate * (1 / M) * sum(cost(mileage, price, M))
    tmpTheta_1 = learningRate * (1 / M) * sum(cost(mileage, price, M, True))
    print(tmpTheta_0, tmpTheta_1)


if __name__ == "__main__":
    dataset = pd.read_csv("./learning/data.csv")
    M = len(dataset)
    mileage = dataset.iloc[0:M, 0]
    price = dataset.iloc[0:M, 1]

    linearRegression(mileage, price, M)
