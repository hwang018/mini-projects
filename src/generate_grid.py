# to generate randomized 2D matrix, for pathfinding
import numpy
from typing import *

# design:
# params:
# m x n rectangle shaped matrix
# start point, end point
# intensity level of obstacles
# guaranteed path/paths

# obstacles represented by 1
# no obstacle is 0

# functions required:
# f -> generate guaranteed path
# f -> generate grids
# f -> apply generated guaranteed path onto grids (sweep out)

import numpy as np
import argparse


def gen_randomized_grids(m: int, n: int, block_intensity: float) -> np.ndarray:
    return np.random.binomial(n=1, p=block_intensity, size=[m, n])


def gen_guaranteed_path(start: tuple, end: tuple) -> None:
    return None


def main(m: int, n: int, block_intensity: float) -> None:
    print(gen_randomized_grids(m, n, block_intensity))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='create basic grid')
    parser.add_argument('--m', type=str, required=True, help='where the model is saved')
    parser.add_argument('--n', type=str, required=True, help='path to the prediction data')
    parser.add_argument('--intensity', type=str, required=True, help='path to the prediction data')

    args = parser.parse_args()
    main(int(args.m), int(args.n), float(args.intensity))
