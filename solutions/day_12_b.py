"""
My solution for the Problem 2 on
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
    the motion of a ship and a waypoint,
    compute the manhattan distance between
    the initial point and the final point of
    the ship.

    :param grp: The list of list of tokens
    :return: The Manhattan distance between the
    source and destination of the ship.

    """

    dire = {"N": 0, "E": 0, "W": 0, "S": 0}
    wpt = {"N": 1, "E": 10}

    def cw_90(x, y):
        """
        Given a coordinate (x, y)
        compute the coordinate that is
        rotated 90 degrees clock-wise
        about the origin.

        :param x: The x-coordinate
        :param y: The y-coordinate

        :return: A tuple (x, y) that
        corresponds to a 90 degree
        clock-wise rotation about the
        origin.

        """
        return (y, -x)

    def ccw_90(x, y):
        """
        Given a coordinate (x, y)
        compute the coordinate that is
        rotated 90 degrees counter
        clock-wise about the origin.

        :param x: The x-coordinate
        :param y: The y-coordinate

        :return: A tuple (x, y) that
        corresponds to a 90 degree
        counter clock-wise rotation
        about the origin.

        """
        return (-y, x)

    for elem in grp:
        c, num = elem[0], int(elem[1:])

        if c == "R":
            for _ in range((num % 360) // 90):
                nw_E, nw_N = cw_90(wpt["E"], wpt["N"])
                wpt["E"], wpt["N"] = nw_E, nw_N

        if c == "L":
            for _ in range((num % 360) // 90):
                nw_E, nw_N = ccw_90(wpt["E"], wpt["N"])
                wpt["E"], wpt["N"] = nw_E, nw_N

        elif c == "F":

            tb_mag, lr_mag = abs(wpt["N"]), abs(wpt["E"])

            top = wpt["N"] >= 0
            right = wpt["E"] >= 0

            if top:
                dire["N"] += num * tb_mag
            else:
                dire["S"] += num * tb_mag
            if right:
                dire["E"] += num * lr_mag
            else:
                dire["W"] += num * lr_mag

        else:
            if c == "N":
                wpt["N"] += num
            elif c == "S":
                wpt["N"] -= num
            elif c == "W":
                wpt["E"] -= num
            elif c == "E":
                wpt["E"] += num

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
