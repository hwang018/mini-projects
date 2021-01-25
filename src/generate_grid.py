import numpy as np


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


def get_grids(m: int, n: int, block_intensity: float, guarantee: str, start: str, end: str) -> np.ndarray:
    """overall function to generate grids, with optional choice to create guaranteed path

    :param m: x axis of matrix
    :param n: y axis of matrix
    :param block_intensity: how much obstacles will appear in grids
    :param guarantee: if a guaranteed path will be generated
    :param start: comma separated point x,y
    :param end: comma separated point x,y
    :return: 2d array with complete grid info for searching and viz
    """
    grids = gen_randomized_grids(m, n, block_intensity)

    if guarantee == "True":
        grids = gen_guaranteed_path(start, end, grids)

    # force start, end to available
    grids[int(start.split(",")[1]), int(start.split(",")[0])] = 0
    grids[int(end.split(",")[1]), int(end.split(",")[0])] = 0

    return grids
