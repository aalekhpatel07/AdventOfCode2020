"""
My solution for the Problem 1 on
Day 16 of Advent of Code 2020.
"""

from functools import reduce
import operator


def read_ranges(_a):
    """
    Given the block of text
    describing the fields and
    its valid ranges, parse the
    input and for every int in the
    valid ranges, record all the different
    fields that are valid for it.

    :param _a: The first block of text
    from AoC Day 16 input.

    :return: A dictionary with ints as keys
    and bool as values representing if the given
    key is contained in some range.

    """

    rngs = []
    for _row in range(len(_a)):
        _, *rest = _a[_row].split(": ")
        r1, r2 = "".join(rest).split(" or ")
        r1s, r1e = list(map(int, r1.split("-")))
        r2s, r2e = list(map(int, r2.split("-")))
        rngs += [(r1s, r1e), (r2s, r2e)]

    bound_end = max([(y, x) for x, y in rngs])
    bound_start = min(rngs)

    _lwr = bound_start[0]
    _upper = bound_end[0]

    result = {i: False for i in range(_lwr, _upper + 1)}

    for (_s, _e) in rngs:
        for _i in range(_s, _e + 1):
            result[_i] = True

    return result


def solve(arr):
    """
    Aaarghhh! Too weird to
    describe. Read AoC Day 16
    problem statement (part 1). This
    solves that problem.

    :param arr: The input for AoC Day 16.

    :return: The sum of those elements from
    the nearby tickets that do not occur in
    any valid range.

    """
    _i = 0
    coll = []
    curr_block = []

    while _i < len(arr):
        if len(arr[_i]) == 0:
            coll.append(curr_block)
            curr_block = []
        else:
            curr_block.append(arr[_i])
        _i += 1

    coll.append(curr_block)
    rngs = read_ranges(coll[0])

    nrby_t = coll[2][1:]
    counter = 0

    for row in nrby_t:
        for elem in map(int, row.split(",")):
            if elem not in rngs or not rngs[elem]:
                counter += elem

    return counter


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
