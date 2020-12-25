"""
My solution for the Problem 1 on
Day 24 of Advent of Code 2020.
"""

from functools import reduce
import operator


# The direction vectors in a hexagonal grid.
hex_directions = {
    "e": (1, 0),
    "se": (0, 1),
    "sw": (-1, 1),
    "ne": (1, -1),
    "nw": (0, -1),
    "w": (-1, 0),
}


def process_group(grp):
    """
    Given a list of
    strings that represent
    some directions, traverse
    along each string in a hexagonal
    tiling and flip the tiles reached
    at the end of each traversal.
    Everytime a tile is flipped it
    changes from black to white or
    white to black.

    :param grp: The list of str.
    :return: The count of the black tiles
    after all strings have been traversed.

    """

    black = set()
    for i in grp:
        tile = parse_string(i)
        if tile in black:
            black -= {tile}
        else:
            black |= {tile}
    return len(black)


def parse_string(s):
    """
    Given a string s of
    six directions:
    'e', 'w', 'ne', 'nw',
    'se', and 'sw' without
    any delimiters, compute
    the final tile reached
    in a hexagonal tiling
    if we start at a center
    (0, 0).

    :param s: An str of directions.
    :return: A tuple (x, y) of ints
    indicating the position of the tile
    reached traversing along the given string
    in this tiling.

    """

    current = (0, 0)
    i = 0
    while i < len(s):
        cx, cy = current
        if s[i] in "we":
            shift_x, shift_y = hex_directions[s[i]]
            i += 1
        elif i < len(s) - 1 and s[i : i + 2] in ("se", "sw", "ne", "nw"):
            shift_x, shift_y = hex_directions[s[i : i + 2]]
            i += 2
        else:
            # In case input incorrectly structured.
            shift_x, shift_y = 0, 0
        current = (cx + shift_x, cy + shift_y)
    return current


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
