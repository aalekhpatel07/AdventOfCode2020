"""
My solution for the Problem 1 on
Day 8 of Advent of Code 2020.
"""

from functools import reduce
import operator


def process_group(grp):
    """
    Given a set of instructions, with commands
    `acc`, `jmp`, or `nop` and values as some
    ints, it is known that if executed,
    it falls in an infinite loop.

    Compute the accumulated value just before
    it falls into recursion.

    :return accumulator, i: The accumulated value
    and the index of instruction that is repeated.

    """
    accumulator = 0

    _i = 0
    _seen = set()

    while True:
        _ins, _val = grp[_i].split(" ")
        _val = int(_val)

        if _i in _seen:
            return accumulator
        _seen |= {_i}
        if _ins == "acc":
            accumulator += _val
            _i += 1
        elif _ins == "jmp":
            _i += _val
        else:
            _i += 1

    return accumulator


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
    Replace this with a nice docstring
    that describes what this function is supposed
    to do.

    :return: The answer required.
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
