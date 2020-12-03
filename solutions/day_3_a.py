"""
My solution for the Problem 1 on
Day 3 of Advent of Code 2020.
"""


def solve(_n, tree):
    """
    Given a list of list of tokens:
    . (empty), or # (tree), compute the
    number of trees one would encounter
    if one traverses the 2D grid along
    a slope of (3, 1).
    :param _n: The number of rows in the
               2D grid.
    :param tree: The 2D grid as a list of list.

    :return: The number of trees encountered on
             a traversal along the slope (3, 1).
    """

    _i, _j = 0, 0
    count = 0

    _col = len(tree[0])

    while _i + 1 < _n:
        _j = (_j + 3) % _col
        _i += 1
        if tree[_i][_j] == "#":
            count += 1

    return count


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.

    """
    _n = int(input())
    arr = []
    for _ in range(_n):
        arr.append(input())

    result = solve(_n, arr)

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
