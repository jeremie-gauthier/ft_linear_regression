from .src.Data import Data
from .src.cost_function import cost_fn

if __name__ == "__main__":
    plots = [Data(1, 1), Data(2, 2), Data(3, 3)]
    print(cost_fn(0, 0, plots))

