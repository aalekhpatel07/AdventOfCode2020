"""
My solution for the Problem 2 on
Day 15 of Advent of Code 2020.
"""

from functools import reduce
import operator


def process_group(grp):
    """
    Given a list containing one list
    of numbers, simulate the process shown
    on AoC Day 15.

    :param grp: The list containing one string
    that looks like a list.

    :return: The final number after the simulation ends.
    """

    nums = list(map(int, grp[0].split(",")))

    prev = {nums[i]: (i + 1, -1) for i in range(len(nums))}

    last = nums[-1]
    _j = len(nums)

    _bound = 30000000

    while _j < _bound:
        (old, older) = prev[last]
        if older == -1:
            last = 0
            prev[last] = (_j + 1, prev[last][0])
        else:
            diff = prev[last][0] - prev[last][1]
            if diff in prev:
                prev[diff] = (_j + 1, prev[diff][0])
            else:
                prev[diff] = (_j + 1, -1)
            last = diff
        _j += 1

    return last


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
