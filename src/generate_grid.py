import numpy as np
import argparse
import matplotlib.pyplot as plt


def gen_randomized_grids(m: int, n: int, block_intensity: float) -> np.ndarray:
    """to generate randomized 2d matrix

    :param m: rectangle x axis
    :param n: rectangle y axis
    :param block_intensity: binomial distribution param to generate blocks range 0 to 1
    :return: 2d array, 1 is obstacle
    """
    return np.random.binomial(n=1, p=block_intensity, size=[m, n])


def gen_guaranteed_path(start: str, end: str, grids: np.ndarray) -> np.ndarray:
    """generate a fixed guaranteed cross-shape path from start to end

    :param start: comma separated x,y
    :param end: comma separated x,y
    :param grids: output from gen_randomized_grids
    :return: modified grids, with garanteed path from start to end
    """
    unblock_x = int(start.split(",")[0])
    unblock_y = int(end.split(",")[1])
    try:
        grids[:, unblock_x] = 0
        grids[unblock_y, :] = 0
    except:
        print("size mismatch")
    return grids


def main(m: int, n: int, block_intensity: float, guarantee: str, start: str, end: str) -> None:
    grids = gen_randomized_grids(m, n, block_intensity)

    if guarantee == "True":
        grids = gen_guaranteed_path(start, end, grids)

    fig, ax = plt.subplots(figsize=(10, 10))

    grids[int(start.split(",")[1]), int(start.split(",")[0])] = 0
    grids[int(end.split(",")[1]), int(end.split(",")[0])] = 0

    ax.imshow(grids, cmap=plt.cm.Paired)

    start_pt = [int(a) for a in start.split(",")]
    end_pt = [int(a) for a in end.split(",")]

    ax.scatter(int(start_pt[0]), int(start_pt[1]), marker=".", color="red", s=100)
    ax.scatter(int(end_pt[0]), int(end_pt[1]), marker=".", color="green", s=100)
    plt.show()
    return grids


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='create basic grid')
    parser.add_argument('--m', type=str, required=True, help='x axis length')
    parser.add_argument('--n', type=str, required=True, help='y axis length')
    parser.add_argument('--intensity', type=str, required=True, help='binomial dist for obstacle intensity')
    parser.add_argument('--guarantee', type=str, required=True, help='if guarantee a path exist from start to end')
    parser.add_argument('--start', type=str, required=False, help='given start point')
    parser.add_argument('--end', type=str, required=False, help='given end point')

    args = parser.parse_args()
    main(int(args.m), int(args.n), float(args.intensity), args.guarantee, args.start, args.end)
