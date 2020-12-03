"""
My solution for the Problem 2 on
Day 3 of Advent of Code 2020.
"""


def solve(_n, tree):
    """
    Given a list of list of tokens:
    . (empty), or # (tree), calculate
    the product of the number of trees
    that one would encounter if one would
    traverse the 2D grid along the given
    set of slopes.

    :param _n: The number of rows in the input.
    :param tree: The list of list of tokens.
    :return: The product of the number of trees
             encountered on every slope.
    """

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    prod = 1
    col = len(tree[0])

    for right, down in slopes:
        _i, _j = 0, 0
        count = 0
        while _i + down < _n:
            _j = (_j + right) % col
            _i += down
            if tree[_i][_j] == "#":
                count += 1
        prod *= count
    return prod


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
