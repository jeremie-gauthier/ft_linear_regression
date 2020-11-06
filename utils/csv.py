import pandas as pd
import sys


def load(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except:
        print(f"Cannot open {filename}", file=sys.stderr)
        sys.exit(-1)


def dataframe(df, column_name):
    try:
        column = df[column_name].values
        return column
    except:
        print(f"Something goes wrong while loading dataframe", file=sys.stderr)
        sys.exit(-1)


def write_thetas(filename, thetas):
    try:
        df = pd.DataFrame({"theta_0": [thetas[0]], "theta_1": [thetas[1]]})
        df.to_csv(filename, mode="w", index=False)
    except:
        print(f"Something goes wrong while writing new thetas", file=sys.stderr)
        sys.exit(-1)
