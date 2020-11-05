from .src.Data import Data
from .src.cost_function import cost_fn

if __name__ == "__main__":
    plots = [Data(0, 0), Data(1, 1), Data(2, 2)]
    # for plot in plots:
    #     print(plot)
    print(cost_fn(0, 0.5, plots))

