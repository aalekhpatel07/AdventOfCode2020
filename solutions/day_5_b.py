"""
My solution for the Problem 2 on
Day 5 of Advent of Code 2020.
"""


def solve(_n, arr):
    """
    Given a list of list of boarding
    passes where each pass is a string
    of 10 characters, where the first
    7 are 'F' or 'B' and the last three
    are 'R' or 'L', find your boarding
    pass if most other boarding passes
    exist and possibly some front rows
    and some back rows may not exist.

    :param arr: The list of list of boarding
    passes.
    :return: The answer required.
    """

    all_seats = {i for i in range(1024)}

    existing = set()

    _i = 0
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
        existing |= {_idx}
        _i += 1

    existing |= {_idx}

    cands = all_seats - existing

    for elem in cands:
        if elem - 1 not in cands and elem + 1 not in cands:
            return elem
    return -1


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
