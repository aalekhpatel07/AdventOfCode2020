"""
My solution for the Problem i on
Day j of Advent of Code 2020.

This is a template that I'll be using
to solve problems.
"""

from functools import reduce
import operator


def process_group(grp):
    """
    Given a group of tokens as a list,
    compute whatever the problem asks
    and return it.

    Example
    ___

    # The problem A of Day 6.

    return len(list(reduce(lambda x, y: x | y, map(set, grp))))

    # The problem B of Day 6.

    return len(list(reduce(lambda x, y: x & y, grp)))

    """

    # grp is a group of tokens.
    # Compute whatever necessary.

    return len(grp)


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
