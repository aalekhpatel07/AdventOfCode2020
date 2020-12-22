"""
My solution for the Problem 2 on
Day 21 of Advent of Code 2020.
"""

from functools import reduce
import operator
from itertools import product
import networkx as nx


def hopcroft_karp(g):
    """
    Given a bipartite graph,
    compute a maximum matching.

    :param g: A networkx graph.
    :return: A dict with keys
    nodes and values their
    corresponding unique
    node in a maximum matching.

    """
    return nx.algorithms.bipartite.matching.hopcroft_karp_matching(g)


def process_group(grp):
    """
    Given a list of list of tokens,
    of the form "A B ... C (contains x, y, z)"
    where A, B, C are strings of ingredients,
    and x, y, z are allergens, determine which
    ingredient contains which unique allergen.

    :param grp: A list of list of tokens.

    :return: A string representing the list of ingredients
    in an alphabetical order of allergens they correspond to.

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

    # Create a map to store which allergen
    # is present in which ingredient.
    aller_to_ing = dict()

    for idx, line in enumerate(grp):
        ing, aller = parse_line(line)

        for a in aller:
            if a not in aller_to_ing:
                # This allergen may be in multiple ingredients.
                aller_to_ing[a] = {x for x in ing}
            else:
                # Keep intersecting these ingredients.
                aller_to_ing[a] &= ing

    # These are the potentially bad ingredients.

    potential = set()
    for x in aller_to_ing.values():
        potential |= x

    # Create a bipartite graph
    # where nodes are allergens and
    # ingredients and there is an edge
    # between two nodes if an allergen
    # may be present in an ingredient.

    g = nx.Graph()
    for aller, ing in aller_to_ing.items():
        for x in ing:
            g.add_edge(aller, x)

    # Compute a maximum matching.
    ans = hopcroft_karp(g)

    # Cherrypick the elements that are potentially bad.
    res = []
    for a in ans:
        if a in potential:
            res.append((ans[a], a))
    # Sort those elements w.r.t their allergen.
    res.sort()
    # Return a result string.
    return ",".join(map(lambda x: x[1], res))


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
