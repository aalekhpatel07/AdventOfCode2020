"""
My solution for the Problem 1 on
Day 13 of Advent of Code 2020.
"""

from functools import reduce
import operator


def process_group(grp):
    """
    Given a list of tokens of tokens
    where the first row is a number
    and the second (also last) row contains
    an `x` or a number separated by ','
    , compute the product of additive inverse of
    some minimum modular residue with its corresponding
    value from the second row.

    :param grp: The list of list of tokens.
    :return: The product of the minimum residue
    with its corresponding value from the second
    row.

    """
    # Get the time of the earliest bus.
    e_time = int(grp[0])

    # Extract all the important bus times.
    bus_ids = list(map(int, [x for x in grp[1].split(",") if x != "x"]))

    # Find the minimum value for bus - (e_time % bus) over all buses.
    # Also keep a track of the corresponding bus
    # as a second component in tuple.

    ans = min([(bus - (e_time % bus), bus) for bus in bus_ids])

    # Return their product.
    return ans[0] * ans[1]


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
