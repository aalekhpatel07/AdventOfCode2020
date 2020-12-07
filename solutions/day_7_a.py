"""
My solution for the Problem 1 on
Day 7 of Advent of Code 2020.
"""

from functools import reduce
import operator
import networkx as nx


def process_group(grp):
    """
    Given a list of list of
    information about what bag
    contains what other bags,
    compute the total number of
    distinctly colored bags that
    contain the 'shiny gold' bag.

    :param grp: The list of list of
    information about the containment
    relationship of bags.

    """

    # Simulate a contains relationship.
    edges = []

    for _i in range(len(grp)):
        node, *rest = grp[_i].split(" bags contain ")
        bags = "".join(map(str, rest)).split(", ")

        for bag in bags:
            if bag == "no other bags.":
                continue
            bag_count, bag_first, bag_last, _ = bag.split(" ")
            bag_name = bag_first + " " + bag_last

            edges.append((node, bag_name, {"weight": int(bag_count)}))

    # Create a Directed Graph.

    g = nx.DiGraph(edges)

    # In this directed graph, count the number of nodes
    # that eventually are in a contains relationship
    # with 'shiny gold'.

    _target = "shiny gold"

    count = 0
    for _n in g.nodes:
        if _n != _target:
            if path_exists(g, _n, _target):
                count += 1
    return count


def path_exists(g, start, end):
    """
    Given a networkx graph g,
    do a dfs and determine if there
    exists a path between start
    and end.

    :return: True if there is a
    path from start to end, False
    otherwise.

    """
    st = []

    visited = set()

    st.append(start)
    while st:
        current = st.pop()

        visited |= {current}

        if current == end:
            return True

        for c in g.neighbors(current):
            if c not in visited:
                st.append(c)

    return end in visited


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
    Replace this with a nice docstring
    that describes what this function is supposed
    to do.

    :return: The answer required.
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
