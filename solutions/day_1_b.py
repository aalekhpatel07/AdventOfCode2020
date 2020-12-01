"""
My solution for the Problem 2 on
Day 1 of Advent of Code 2020.
"""


def solve(arr):
    """
    Given an array of positive ints,
    find the product of three numbers that
    sum to 2020.

    :param arr: The array of positive ints.

    :return: The product of the only three
             numbers in arr that sum to 2020.
    """

    _s = dict()

    for _i, vali in enumerate(arr):
        for _j, valj in enumerate(arr):
            if _i >= _j:
                continue

            if vali + valj in _s:
                _s[vali + valj] |= {(_i, _j)}
            else:
                _s[vali + valj] = {(_i, _j)}

    for _z, val in enumerate(arr):
        _t = 2020 - val
        if _t in _s:
            for e_i, e_j in _s[_t]:
                if _z not in (e_i, e_j):
                    return val * arr[e_i] * arr[e_j]

    return -1


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    _n = int(input())
    arr = []
    for _ in range(_n):
        arr.append(int(input()))
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
