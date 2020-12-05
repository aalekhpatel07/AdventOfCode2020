"""
My solution for the Problem 1 on
Day 5 of Advent of Code 2020.
"""


def solve(_n, arr):
    """
    Given a list of list of boarding
    passes determine the one with largest
    id where id is given by 8 * row + col
    where row is given by a string of 7 characters
    and col is given by a string of 3 characters
    ultimately forming a binary string.

    :param arr: The list of list of boarding passes.
    :return: The highest id of a boarding pass.

    """
    _i = 0
    _best = -1
    while _i < _n:
        token = arr[_i]
        _row = 0
        _col = 0
        for _j in range(7):
            if token[_j] == "B":
                _row += 2 ** (6 - _j)
        for _z in range(3):
            if token[7 + _z] == "R":
                _col += 2 ** (2 - _z)
        _idx = _row * 8 + _col
        _best = max(_best, _idx)
        _i += 1

    _best = max(_best, _idx)

    return _best


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
