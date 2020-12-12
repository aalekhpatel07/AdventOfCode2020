"""
My solution for the Problem 1 on
Day 12 of Advent of Code 2020.
"""

from functools import reduce
import operator


def process_group(grp):
    """
    Given a list of list of tokens
    where each token starts with a
    character from 'NSEWLRF', and
    ends with a number, that describe
    the motion of a ship and the direction
    it faces at any given point in time,
    compute the manhattan distance between
    the initial point and the final point of
    the ship.

    :param grp: The list of list of tokens.
    :return: The Manhattan distance between
    the source and destination of the ship.

    """

    dire = {"N": 0, "E": 0, "W": 0, "S": 0}

    ship_dir_options = ["E", "S", "W", "N"]

    current_dir_idx = 0

    for elem in grp:
        c, num = elem[0], int(elem[1:])
        if c == "R":
            current_dir_idx = (current_dir_idx + num // 90) % 4
        elif c == "L":
            current_dir_idx = (current_dir_idx - num // 90) % 4
        elif c == "F":
            dire[ship_dir_options[current_dir_idx]] += num
        else:
            dire[c] += num

    dist_ver = abs(dire["N"] - dire["S"])
    dist_hor = abs(dire["E"] - dire["W"])

    man_dist = dist_ver + dist_hor

    return man_dist


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
