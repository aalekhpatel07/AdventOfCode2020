"""
My solution for the Problem 2 on
Day 6 of Advent of Code 2020.
"""


def solve(arr):
    """
    Given a list of list of tokens
    where each token is a set of
    characters, sum the length of
    the intersections between every
    newline separated token groups.
    :return count: The sum of the
    intersection lengths.
    """
    _i = 0
    count = 0
    tokens = []
    while _i < len(arr):
        if arr[_i] == "":
            res = {_z for _z in tokens[0]}
            for _t in range(len(tokens)):
                res = res.intersection({_z for _z in tokens[_t]})
            count += len(list(res))
            tokens = []
        else:
            tokens.append([_z for _z in arr[_i]])

        _i += 1

    res = {_z for _z in tokens[0]}
    for _t in range(len(tokens)):
        res = res.intersection({_z for _z in tokens[_t]})
    count += len(list(res))

    return count


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
