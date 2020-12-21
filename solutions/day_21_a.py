"""
My solution for the Problem 1 on
Day 21 of Advent of Code 2020.
"""

from functools import reduce
import operator
from itertools import product


def process_group(grp):
    """
    Given a list of list of tokens,
    of the form "A B ... C (contains x, y, z)"
    where A, B, C are strings of ingredients,
    and x, y, z are allergens, determine the
    count of the ingredients that definitely
    do not contain any allergens.

    :param grp: A list of list of tokens.
    :return: A count of the occurrences of
    "good"(allergen-free) ingredients.

    """

    def parse_line(s):
        """
        Given a single token
        of the form
        "A B ... C (contains x, y, z)"
        parse it and return a set of
        ingredients and its corresponding
        allergens.

        :param s: A string representing token.
        :return a, b: A tuple of sets representing
        the ingredients and allergens.
        """
        s = s.replace(" (", " ").replace(", ", " ").replace(")", " ")
        ingredients, allergens = s.split(" contains ")
        a = set(ingredients.split(" "))
        b = set(allergens.split(" ")) - {""}
        return a, b

    aller_to_ing = dict()
    computed = []

    for idx, line in enumerate(grp):
        ing, aller = parse_line(line)
        computed.append((set(x for x in ing), set(a for a in aller)))

        for a in aller:
            if a not in aller_to_ing:
                aller_to_ing[a] = {x for x in ing}
            else:
                aller_to_ing[a] &= ing

    # Potentially bad ingredients.
    potential = set()
    for x in aller_to_ing.values():
        potential |= x

    counter = 0

    for ing, aller in computed:
        for x in ing:
            if x not in potential:
                counter += 1

    return counter


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
