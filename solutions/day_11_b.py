"""
My solution for the Problem 2 on
Day 11 of Advent of Code 2020.
"""

from functools import reduce
import operator
import copy


def process_group(grp):
    """
    Given a list of list of tokens,
    each '.', '#', or 'L', simulate
    a Game of Life using some rules.
    Then compute the frequency of '#'
    after the game stabilizes.

    :param grp: The list of list of tokens.

    Rules
    ____

    i) 'L' changes to '#' if its
        neighborhood has no other
        L's.
    ii) '#' changes to 'L' if its
        neighborhood has at least
        5 'L's.

    Neighborhood: The first 'L' or '#'
    in all of the 8 directions.

    Compute the frequency of '#'
    after the simulation stabilizes.
    """

    temp = []
    for x in grp:
        temp.append(list(x))

    grp = temp

    def nbs(i, j, m, n, arr):
        """
        Given the row and col bounds
        `m` and `n`, compute the set of
        neighbors of (i, j).

        :param i: The row index.
        :param j: The column index.
        :param m: The total number of rows.
        :param n: The total number of columns.

        :return res: A set of tuples of neighbors
        of (i, j).
        """

        res = set()

        def get_strip(start_x, start_y, shift_x, shift_y):
            """
            Given a starting coordinate and the shifts in either
            directions, determine the first occurrence of '#'
            on that line.

            :param start_x: The starting x index.
            :param start_y: The starting y index.
            :param shift_x: The shift in x (rows up/down).
            :param shift_y: The shift in y (columns left/right).

            :return st: The first '#' on this line segment if exists,
             empty set otherwise.
            """
            st = set()

            bound_x = len(arr)
            bound_y = len(arr[0])

            if not 0 <= start_x < bound_x or not 0 <= start_y < bound_y:
                return st

            while arr[start_x][start_y] == ".":
                start_x += shift_x
                start_y += shift_y
                if not 0 <= start_x < bound_x or not 0 <= start_y < bound_y:
                    break

            if not 0 <= start_x < bound_x or not 0 <= start_y < bound_y:
                return st
            else:
                st |= {(start_x, start_y)}
            return st

        for z in (-1, 0, 1):
            for y in (-1, 0, 1):
                if z == 0 and y == 0:
                    continue
                res |= get_strip(i + z, j + y, z, y)

        return res - {(i, j)}

    def flip(arr):
        """
        Given a list of list of tokens
        simulate the game of life according
        to the rules.

        :param arr: The list of list of tokens.
        """

        fpd = copy.deepcopy(arr)

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == ".":
                    continue
                ct = 0
                for (z, y) in nbs(i, j, len(arr), len(arr[i]), arr):
                    if arr[z][y] == "#":
                        ct += 1
                if arr[i][j] == "L" and ct == 0:

                    fpd[i][j] = "#"
                elif arr[i][j] == "#" and ct >= 5:

                    fpd[i][j] = "L"
        return fpd

    def count_occ(a):
        """
        Compute the frequency
        of '#' in a list of list `a`.

        :param a: The list of list of tokens.

        :return: The number of times
        `#` occurs in a.
        """
        res = 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == "#":
                    res += 1
        return res

    curr = count_occ(grp)
    prev = -1

    while curr != prev:
        grp = flip(grp)
        prev = curr
        curr = count_occ(grp)
    return curr


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
