"""
My solution for the Problem 1 on
Day 19 of Advent of Code 2020.
"""

import operator
from itertools import product as p


def split_rules_and_strings(arr):
    """
    Given a list of strings,
    representing the rules
    and the query strings,
    split the rules and strings
    into a dictionary and a list
    for further use.

    :param arr: A list of strings.
    :return: A tuple of dict and list
    representing the ruleset and the
    query strings.
    """
    rules = dict()
    string_time = False
    strings = []
    for idx, elem in enumerate(arr):
        if elem == "":
            string_time = True
        elif not string_time:
            head, *rest = elem.split(": ")
            rules[int(head)] = "".join(rest)
        else:
            strings.append(elem)
    return rules, strings


_DEPTH_MAX = 20


def generate_rules(rules, current, depth=0):
    """
    Generate all the strings that
    can be produced from a given ruleset.

    :param rules: A dict with keys as ints,
    and values as a string representing a rule.
    :param current: An int, representing the current
    ruleset under consideration.
    :param depth: A helper parameter that stops
    unnecessary recursion if there is a loop in the ruleset.

    :yield: An str object that matches the ruleset defined
    for "current".
    """
    if depth > _DEPTH_MAX:
        # Too deep. Probably a loop exists.
        return
    elif rules[current] in ('"a"', '"b"'):
        # Base cases.
        yield rules[current][1:2]
    else:
        # For each group we must union the set of strings formed.
        for group in rules[current].split(" | "):
            # Combine the solution from children and yield
            # all possible strings that match.
            for cmb in p(
                *[generate_rules(rules, int(m), depth + 1) for m in group.split()]
            ):
                yield "".join(cmb)


def solve(grp):
    """
    Given a list of strings,
    representing the ruleset
    and query strings,
    solve the problem of AoC
    2020 (day 19).

    :param grp: A list of str.
    :return: The count of query
    strings that match to ruleset 0.
    """

    rules, strings = split_rules_and_strings(grp)
    zero = set(generate_rules(rules, 0))
    res = 0
    for s in strings:
        if s in zero:
            res += 1
    return res


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
