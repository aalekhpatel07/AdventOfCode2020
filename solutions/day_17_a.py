"""
My solution for Problem 1
on Day 17 of Advent of Code 2020.
"""

from functools import reduce
import operator
import copy
import numpy as np
from itertools import product


DIMENSIONS = 3

# Use DIMENSIONS = 4 for part b).

# GRID_SIZE indicates what size the grid will be simulated.
# Each coordinate will have values in range [-GRID_SIZE // 2, GRID_SIZE // 2)
# 19 gave correct answer and 18 did not.
# So use 19.

GRID_SIZE = 21

# The smaller the grid_size the faster the simulation.
# However, we need grid to be big enough to
# account for 6 cycles. Hence GRID_SIZE must be >= 19.


def sanitize_to_numpy(grp):
    """
    Given some initial data
    about a 2D-set of points,
    initialize a `DIMENSIONS`-dimensional
    ndArray that has at its center
    the given 2D-set of points.

    :param grp: A list of list of tokens,
    each '#' or '.'.

    :return: A numpy ndArray object of
    dimension `DIMENSIONS` with the
    given list of list projected onto
    the center of the simulated grid.

    """

    _center = GRID_SIZE // 2
    temp = list(map(list, grp))
    grid = np.array(["." for _ in range(GRID_SIZE ** DIMENSIONS)])
    grid = grid.reshape((GRID_SIZE,) * DIMENSIONS)

    for idx, row in enumerate(temp):
        for jdx, elem in enumerate(row):
            x_pos = _center - len(temp) // 2 + idx
            y_pos = _center - len(row) // 2 + jdx
            f_idx = (x_pos, y_pos) + (_center,) * (DIMENSIONS - 2)

            grid[f_idx] = elem

    return grid


def nbs(*args):
    """
    Given a coordinate v = (i, j, k, ...)
    compute the set of neighbors
    x = (xi, xj, xk, ...) such that
    ||v - x|| <= 1 and x != v where
    ||u|| = sum(|ui| + |uj| + ...).

    :param args: A list of arguments
    i, j, k, ...

    :return: The set of neighbors of (i, j, k, ...)
    in a `len(args)`-dimensional grid.

    Notes
    ____

    Essentially, for a "centered enough"
    coordinate, its neighbors form a set
    of 3 ** DIMENSIONS - 1 points.

    """

    res = set()
    for tpl in product(*([range(-1, 2)] * len(args))):
        if max(tpl) == min(tpl) == 0:
            continue
        else:
            res |= {tuple((tpl[_i] + args[_i] for _i in range(len(args))))}
    return res


def flip(arr):
    """
    Given a numpy multidimensional list
    simulate the game of life according
    to the rules given above.

    :param arr: A numpy ndArray object.
    :return: A numpy ndArray object after
    simulating one cycle of the rules.
    """

    fpd = copy.deepcopy(arr)

    for tpl in product(*[range(GRID_SIZE) for _ in range(DIMENSIONS)]):
        ct = 0
        for neighbor in nbs(*list(tpl)):
            if 0 <= min(neighbor) <= max(neighbor) < GRID_SIZE:
                if arr[neighbor] == "#":
                    ct += 1
        if arr[tpl] == "." and ct == 3:
            fpd[tpl] = "#"
        elif arr[tpl] == "#" and ct not in (2, 3):
            fpd[tpl] = "."

    return fpd


def count_occ(a):
    """
    Compute the frequency
    of '#' in a numpy ndArray.

    :param a: A numpy ndArray object.

    :return: The number of times
    `#` occurs in a.
    """
    return np.count_nonzero(a == "#")


def process_group(grp):
    """
    Given a numpy ndArray of tokens,
    each '.', '#', simulate
    a Game of Life using the rules
    defined below. Compute the
    frequency of '#' after the game
    stabilizes.

    :param grp: A numpy ndArray object of
    tokens.

    Rules
    ____

    i) '.' changes to '#' if its
        neighborhood has exactly 3
        L's.

    ii) '#' changes to '.' if its
        neighborhood either has at
        most 1 '.' or at least 4 '.'


    Neighborhood: The immediately adjacent
    squares satisfying ||x - y|| <= 1 where
    the norm is the Taxicab distance.

    Compute the frequency of '#'
    after the simulation stabilizes.

    :return: The frequency of '#'
    after the simulation stabilizes.

    """

    grid = sanitize_to_numpy(grp)
    _cycles = 6

    for _ in range(_cycles):
        grid = flip(grid)

    return count_occ(grid)


def reducer():
    """
    Define how to reduce the
    groups.

    Example
    ___

    return lambda x, y: x + y
    OR
    return lambda x, y: x * y
    OR
    return operator.multiply
    """

    return operator.add


# There's absolutely no need to touch any function below this line!
# STOP!!!


def solve(arr):
    """
    Given a list of lists
    possibly separated by newlines,
    'process' each group of lists
    and reduce it to a result based
    on the operator defined above.

    :param arr: The list of list.
    :return: The reduced map based on `operator()`.

    """

    _i = 0
    _group = []
    group_results = []

    while _i < len(arr):
        if arr[_i] == "":
            group_results.append(process_group(_group))
            _group = []
        else:
            _group.append(arr[_i])
        _i += 1

    group_results.append(process_group(_group))
    final_result = reduce(reducer(), group_results)

    return final_result


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.

    """

    _n = int(input())
    arr = []
    for _ in range(_n):
        arr.append(input())

    result = solve(arr)
    print(result)
    return result


def main():
    """
    Carry forward the output of driver.
    :return: The output of driver.
    """
    return driver()


if __name__ == "__main__":
    main()
