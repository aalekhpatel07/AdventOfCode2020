"""
My solution for the Problem 1 on
Day 14 of Advent of Code 2020.
"""

from functools import reduce
import operator


def _apply_mask(_m, _val):
    """
    Given a mask `_m` that is
    a string of 36 bits each '0',
    '1' or 'X', apply it to a given
    value.

    :param _m: The mask string
    :param _val: A value to be masked.

    :return: The uniqued masked value.

    """
    _v = str(bin(int(_val)))[2:]

    _v = ["0"] * (36 - len(_v)) + list(_v)

    for _i in range(len(_m)):
        if _m[_i] == "X":
            continue
        else:
            _v[_i] = _m[_i]
    _res = "".join(_v)

    return int(_res, 2)


def process_group(grp):
    """
    Given a list of list of tokens
    where each token is either `mask = XX0101X...`
    or `mem[address] = value`, simulate whatever
    day 14 has in its description.

    :param grp: The list of list of tokens.

    :return: The sum of all values left in memory
    after the process is simulated.
    """

    mask = ""
    space = dict()

    for _ins in grp:
        if _ins.startswith("mask"):
            mask = _ins.split(" = ")[1]
        else:
            mem, value = _ins.split(" = ")
            address = mem[4:-1]
            space[address] = _apply_mask(mask, value)
    return sum(space.values())


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
