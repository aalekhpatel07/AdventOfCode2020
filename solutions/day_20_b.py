"""
My solution for the Problem 2 on
Day 20 of Advent of Code 2020.
"""

from pathlib import Path
import os
from functools import reduce
from itertools import product
from copy import deepcopy as dc


def parse_images(grp):
    """
    Read the input data into titles and
    images.
    """
    images = []
    titles = []

    for i in range(len(grp) // 11):
        _title = int(grp[11 * i][:-1].split(" ")[1])
        titles.append(_title)
        images.append(grp[11 * i + 1 : 11 * (i + 1)])
    return titles, images


def get_all_transforms(titles, data):
    """
    Given a list of titles and
    tile data associated to each title,
    compute a dictionary that has as keys
    the unique titles and as values, a
    list of rotations and flips of each tile
    that is associated to each title.

    :param titles: A list of tile ids.

    :param data: A list of 2D lists that
    represent blocks in the data.

    :return: A dictionary of tile ids and
    its corresponding collection of flips
    and rotations.

    """
    res = dict()

    for title, d in zip(titles, data):
        res[title] = transform(d)
    return res


def transform(arr):
    """
    Given a 2D list,
    rotate and flip it in
    all possible ways and return
    a collection of the views after
    simulating such flips and
    rotations.

    :param arr: A 2D list
    :return: A list of rotations
    and flips of arr.

    """
    # One flip and 4 rotations.
    res = []
    curr = dc([list(x) for x in arr])
    res.append(curr)

    for _ in range(3):
        curr = rotate_right(curr)
        res.append(dc(curr))

    curr = flip_transpose(arr)

    for _ in range(4):
        curr = rotate_right(curr)
        res.append(dc(curr))

    return res


def rotate_right(arr):
    """
    Rotate a copy of given 2D list
    clockwise by 90 degrees
    and return a new list.

    :param arr: A 2D-list of arbitrary
    dimensions.

    :return: A list that is "arr" rotated
    90 degree clockwise by its center.
    """
    n = len(arr)
    m = len(arr[0])

    res = [[None for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j] = arr[n - j - 1][i]

    return res


def flip_transpose(arr):
    """
    Flip a 2D-list (i.e. transpose).
    """
    m = len(arr)
    n = len(arr[0])
    res = [[-1 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            res[i][j] = arr[j][i]
    return res


def remove_border(chonk):
    """
    Remove the borders of a 2D list.
    """
    res = []
    for i in range(1, len(chonk) - 1):
        temp = []
        for j in range(1, len(chonk[i]) - 1):
            temp.append(chonk[i][j])
        res.append(dc(temp))
    return res


def count(grid, c):
    """
    Count the occurrences
    of an object "c" in
    the 2D list "grid".
    """
    acc = 0
    for row in grid:
        for elem in row:
            acc += c == elem
    return acc


def find_monster(grid, mon):
    """
    Given a grid and a list of
    indices of monster,
    find the number of "#" that
    are not part of any monster.

    :param grid: An (8 * 12) x (8 * 12)
    list of chars.
    :param mon: A list of indices of
    the monster.

    :return: The count of "#" that
    are not part of any sea monster.
    """

    monster_pounds = set()

    for t in transform(grid):
        # Monster is of height 2.
        for i in range(len(grid) - 2):
            # Monster is of width 19.
            for j in range(len(grid[i]) - 19):

                # Check all legal candidates for monsters.
                cands = [grid[x + i][y + j] for x, y in mon]

                # If monster found, update its set of indices.
                if cands.count("#") == len(mon):
                    monster_pounds |= {(x + i, y + j) for x, y in mon}

    # Unique monster-free squares that are "#".
    ans = count(grid, "#") - len(monster_pounds)
    return ans


def solve(grp):
    """
    Given some blocks of 10 x 10
    tiles, compute the number of sea monsters
    and yadi-yada.... See AoC (2020) Day 20.
    """

    # data computed from part a.
    res = get_all_transforms(*parse_images(grp))

    TOP = Path("data/input")

    result = [[None for _ in range(12)] for _ in range(12)]

    with open(TOP / "day_20_b_image.txt", "r") as f:
        for line in f.readlines():
            i, j, title, tile_idx = line.strip().split(" ")
            result[int(i)][int(j)] = dc(res[int(title)][int(tile_idx)])

    # Remove border.
    no_border = [[None for _ in range(12)] for _ in range(12)]
    for i in range(12):
        for j in range(12):
            no_border[i][j] = dc(remove_border(result[i][j]))

    # Transform 12 x 12 x 8 x 8 into 96 x 96.
    s_clean = [[None for _ in range(96)] for _ in range(96)]

    for x in range(12):
        for y in range(12):
            for z in range(8):
                for w in range(8):
                    s_clean[8 * x + z][8 * y + w] = no_border[x][y][z][w]

    # Indices of the sea monster.
    sea_monster = [
        (0, 18),
        (1, 0),
        (1, 5),
        (1, 6),
        (1, 11),
        (1, 12),
        (1, 17),
        (1, 18),
        (1, 19),
        (2, 1),
        (2, 4),
        (2, 7),
        (2, 10),
        (2, 13),
        (2, 16),
    ]

    return find_monster(dc(s_clean), sea_monster)


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.

    """

    _n = int(input())
    arr = []
    for _ in range(_n):
        temp = input()
        if temp:
            arr.append(temp)

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
