"""
My solution for the Problem 2 on
Day 24 of Advent of Code 2020.
"""

from functools import reduce
import operator
from copy import deepcopy as dc


# The direction vector for hexagonal tiles.
hex_directions = {
    "e": (1, 0),
    "se": (0, 1),
    "sw": (-1, 1),
    "ne": (1, -1),
    "nw": (0, -1),
    "w": (-1, 0),
}


def nbs(x, y):
    """
    Given a coordinate x, y
    return the set of its neighbors
    that are immediately adjacent to it
    on a hexagonal tiling.

    :param x: An int, representing the x-coordinate.
    :param y: An int, representing the y-coordinate.

    :return: A set of tuples representing
    coordinates that are immediately adjacent
    to (x, y) in a hexagonal tiling.

    """
    res = set()
    for k in hex_directions:
        shift_x, shift_y = hex_directions[k]
        res |= {(x + shift_x, y + shift_y)}
    return res


def game_of_life(black):
    """
    Given a set of tiles that are black,
    simulate the game of life for every day
    using the following rules:

    i.) If a tile is black and either 0
        or more than two of its neighbors
        are black then it flips to white.
    ii.) If a tile is white and exactly
        two of its neighbors are black then
        it flips to white.

    Here, neighbors of a tile denote any of its
    six immediately adjacent hexagonal tiles.

    :param black: A set of tuples, representing
    the coordinates of black tiles relative to
    a center tile (0, 0).
    :return: The number of black tiles after
    day 100.
    """

    for day in range(100):
        candidates = set()
        next_black = dc(black)

        for x, y in black:
            candidates |= nbs(x, y)
            candidates |= {(x, y)}

        to_white = set()
        to_black = set()

        for x, y in candidates:
            black_count = sum((a, b) in black for a, b in nbs(x, y))
            if (x, y) in black and black_count not in (1, 2):
                to_white |= {(x, y)}
            elif (x, y) not in black and black_count == 2:
                to_black |= {(x, y)}

        # Some black tiles will turn white so remove them.
        next_black -= to_white

        # Some black tiles will turn black so union them.
        next_black |= to_black

        # Update black tiles.
        black = next_black

    return len(black)


def process_group(grp):
    """
    After traversing the strings
    from part 1), all the tiles
    flip according to the following
    rules every day:

    i.) If a tile is black and either 0
        or more than two of its neighbors
        are black then it flips to white.
    ii.) If a tile is white and exactly
        two of its neighbors are black then
        it flips to white.

    Compute the number of black tiles after day 100.

    :param grp: The list of string directions.
    :return: An int, representing the count of black
    tiles after the flipping process terminates on day 100.
    """

    black = set()
    for s in grp:
        tile = parse_string(s)
        if tile in black:
            black -= {tile}
        else:
            black |= {tile}

    return game_of_life(black)


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
            # In case input is structured incorrectly.
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
