"""
My solution for the Problem 2 on
Day 19 of Advent of Code 2020.
"""

from functools import reduce
import operator
from itertools import product as p
from random import choice


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
        return
    elif rules[current] in ('"a"', '"b"'):
        yield rules[current][1:-1]
    else:
        for group in rules[current].split(" | "):
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
    strings that match to ruleset 0
    after some modification.

    """

    rules, strings = split_rules_and_strings(grp)

    thirty_one = set(generate_rules(rules, 31))
    forty_two = set(generate_rules(rules, 42))

    # Rule 8: 42 | 42 8
    # means that the rule 8
    # is satisfied if any positive
    # number of blocks of rule 42
    # are satisfied.

    # Rule 11: 42 31 | 42 11 31
    # means that the rule 11
    # is satisfied if any positive
    # number of blocks of rule 42
    # are followed by some positive
    # number of blocks of rule 31.

    # To fit the ruleset for 31 or 42,
    # all strings have to be of the same fixed
    # length.

    # Finally, to match 0, we must match
    # any positive number of blocks of 42,
    # followed by some positive number of blocks
    # of 31.

    expected_size = len(choice(list(thirty_one)))
    res = 0

    for s in strings:
        # Only worry if the query
        # string can be divided into
        # blocks of size "expected_size".
        if len(s) % expected_size == 0:
            blocks_thirty_one = []
            blocks_forty_two = []

            for i in range(0, len(s), expected_size):
                # collect all blocks of a fixed size
                blocks_thirty_one.append(s[i : i + expected_size] in thirty_one)
                blocks_forty_two.append(s[i : i + expected_size] in forty_two)

            # Check only the upper half as the lower
            # half is already determined by ruleset 8.

            _i = len(blocks_forty_two) // 2 + 1
            while _i < len(blocks_forty_two):
                # Check if some 42s are followed by some 31s.
                if all(blocks_forty_two[:_i]) and all(blocks_thirty_one[_i:]):
                    # The first one we can find validates the string.
                    # So count it and jump to the next query string.
                    res += 1
                    break
                _i += 1
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
