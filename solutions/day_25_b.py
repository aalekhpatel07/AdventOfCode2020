"""
There was no new problem on Day 25 after
solving the first one.

This is the same script as for problem 1.

"""

from functools import reduce
import operator


def dlog(g, n, p):
    """
    Find an int a
    such that
    ((g ** a) % p) == n.

    :param g: A primitive root modulo p.
    :param n: A residue modulo p.
    :param p: A prime.

    :return: An int "a", i.e.
    the solution to (g ** a) = n (mod p)
    if it exists.
    """

    i = 1
    while i < p:
        if pow(g, i, p) == n:
            return i
        i += 1

    return -1


def process_group(grp):
    """
    Given two ints in a list,
    solve the Diffie-Hellmann
    problem for them with a fixed
    prime "p", and a fixed primitive
    root "g".

    :return: The shared private key.
    """

    sd, sc = list(map(int, grp[0:2]))
    p = 20201227
    g = 7

    # 8912970 1050835

    # In case it takes long, the
    # answer is above.

    # d = dlog(g, sd, p)
    # c = dlog(g, sc, p)

    d = 8912970
    c = 1050835

    return pow(g, c * d, p)


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
