"""
My solution for the Problem 1 on
Day 6 of Advent of Code 2020.
"""


def solve(arr):
    """
    Given a list of list of tokens
    where each token is a set of
    characters, sum the length of
    the unions between every
    newline separated token groups.
    :return count: The sum of the unions
    of the token groups.

    """
    i = 0
    count = 0
    tokens = []

    while i < len(arr):
        if arr[i] == "":

            res = {z for z in tokens[0]}
            for t in range(len(tokens)):
                res |= {z for z in tokens[t]}
            count += len(list(res))
            tokens = []
        else:
            tokens.append([z for z in arr[i]])

        i += 1

    res = {z for z in tokens[0]}
    for t in range(len(tokens)):
        res |= {z for z in tokens[t]}
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
