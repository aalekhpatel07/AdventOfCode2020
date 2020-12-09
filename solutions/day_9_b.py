"""
My solution for the Problem 2 on
Day 9 of Advent of Code 2020.
"""

from functools import reduce
import operator


def process_group(grp):
    """
    Given a list of list of ints,
    compute the sum of a minimum
    and a maximum value of a contiguouos
    sublist that sums to a given target.

    :param grp: The list of list of ints.
    :return: The sum of min and max value
    from some contiguous sublist that sum
    to 1504371145.

    """

    TARGET = 1504371145

    arr = list(map(int, grp))

    for shift in range(2, len(arr)):
        i = 0
        ctgs_sum = sum(arr[i : i + shift])

        if ctgs_sum == TARGET:

            best_min = min(arr[i : i + shift])
            best_max = max(arr[i : i + shift])

            return best_min + best_max

        while i < len(arr) - shift - 1:
            to_go = arr[i]
            to_come = arr[i + shift]

            ctgs_sum += to_come - to_go

            if ctgs_sum == TARGET:
                rng = arr[i + 1 : i + shift + 1]
                return min(rng) + max(rng)
            else:
                i += 1

    return -1


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
    Given a list of list of ints
    that are potentially separeted
    by newlines, for each group,
    compute the sum of the min-max
    values in a contiguous sublist.

    :param arr: The list of list of ints.

    :return: The sum of the solution to each group.
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
