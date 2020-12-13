"""
My solution for the Problem 2 on
Day 13 of Advent of Code 2020.
"""

from functools import reduce
import operator


def process_group(grp):
    """
    Given a list of tokens of tokens
    where each token is an `x` or a
    number, compute the minimum value
    of t such that:

    For all indices i such that arr[i] != 'x':
    it is the case that

            t = 0 mod (arr[i] - i)

    This is a modular congruence that can be
    solved by using the Chinese Remainder Theorem.

    """
    e_time = int(grp[0])

    buses = grp[1].split(",")
    size = len(buses)

    mod_pairs = []

    for i in range(size):
        if buses[i] == "x":
            continue
        mod_val = int(buses[i])
        residue_val = (mod_val - i) % mod_val
        if residue_val == 0:
            mod_pairs.append((mod_val, mod_val))
        else:
            mod_pairs.append((residue_val, mod_val))

    def extended_euclidean(a, b):
        """
        Given two ints a, b
        find a tuple of ints p, q
        such that a*p + b*q = 1.

        :param a: A positive int.
        :param b: A positive int.

        :return: A tuple of ints
        (p, q) such that

            a * p + b * q = 1.

        """
        if not b:
            return (1, 0)

        x, y = extended_euclidean(b, a % b)

        fct = a // b

        return (y, x - fct * y)

    def chinese_remainder_theorem(n1, n2):
        """
        Given a system of modular congruences
        of size two:

        t = x1 mod m1
        t = x2 mod m2

        Compute the smallest positive int t
        that satisifes this system.

        :param n1: A tuple representing (x1, m1)
        :param n2: A tuple representing (x2, m2)

        Notes
        ____

        The Chinese Remainder Theorem requires
        that gcd(m1, m2) = 1. Otherwise, a
        solution is not even guaranteed.

        :return: A tuple (t, m1*m2) where t is
        the smallest positive int that satisfies
        the above system of modular congruences.

        """
        # Extract.

        x1, m1 = n1
        x2, m2 = n2

        # Compute x, y such that m1 * x + m2 * y = 1.
        (x, y) = extended_euclidean(m1, m2)

        # The Chinese Remainder Theorem says the final
        # result is always mod m1*m2.

        # The modular residue is x2 * m1 * x + x1 * m2 * y.

        m_final = m1 * m2
        x_final = x2 * m1 * x + x1 * m2 * y

        # Return the result as a tuple (x_final, m_final)
        return ((x_final % m_final + m_final) % m_final, m_final)

    # To solve a larger system of modular congruences
    # we can reduce the nums array using the Chinese Remainder Theorem.

    # It is required that all mod values in the nums be pairwise
    # relatively prime otherwise the answer is not guaranteed to be correct.

    # It can be verified by pairwise gcd computation for all the
    # mod values in nums that gcd(x, y) = 1 for every distinct pair
    # of mod values x, and y.

    residue, modular = reduce(chinese_remainder_theorem, mod_pairs)

    # Reducing the solution using the two-pair CRT
    # we get the smallest value of positive t
    # that satisfies all the modular congruences in
    # `mod_pairs`.

    return residue


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
