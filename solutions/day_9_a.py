"""
My solution for the Problem 1 on
Day 9 of Advent of Code 2020.
"""

from functools import reduce
import operator


def process_group(grp):
    """

    Given a list of list of ints,
    find the first record with the property
    that it cannot be represented as a paired
    sum of 25 consecutive records above it.

    :param grp: The list of list of ints.
    :return: The first entry that satisfies
    the given property.

    """

    def check_preamble(_pr, _num):
        """
        Given a list of 25 consecutive entries,
        compute if there exist two distinct entries
        that sum to `_num`.

        :param _pr: A sublist of `grp`.
        :param _num: The target sum.

        """
        for i in range(25):
            for j in range(i + 1, 25):
                if _pr[i] + _pr[j] == _num:
                    return True
        return False

    grp = list(map(int, grp))
    _preamble = list(map(int, grp[:25]))

    for i in range(25, len(grp)):
        current = grp[i]
        if not check_preamble(_preamble, current):
            return current
        else:
            _preamble.pop(0)
            _preamble.append(int(current))

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
    find the first number that cannot be
    written as a sum of some two numbers
    in the previous 25 numbers.

    :return: The first number that satisfies
    this property.

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
