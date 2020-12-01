"""
My solution for the Problem 1 on
Day 1 of Advent of Code 2020.
"""


def solve(arr):
    """
    Given an array of positive ints,
    find the product of two numbers that
    sum to 2020.

    :param arr: The array of positive ints.

    :return: The product of the only two
             numbers in arr that sum to 2020.
    """
    _s = set(arr)
    for _i in _s:
        if 2020 - _i in _s:
            return _i * (2020 - _i)

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
