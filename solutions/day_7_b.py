"""
My solution for the Problem i on
Day j of Advent of Code 2020.
This is a template that I'll be using
to solve problems.
"""

from functools import reduce
import operator
import networkx as nx


def helper(g, memo, start, current, parent):
    """
    Given a directed tree `g`, its root `current`,
    where nodes represent bags of different color,
    compute the total number of bags contained in
    the bag with color `shiny gold`.

    :return memo: A dictionary with the keys as nodes
    and the values as the number of bags of different colors
    that are fully contained in a single bag of that color.

    """

    # If the current bag is a leaf, we say it contributes nothing
    # because we only store about what a certain bag fully contains
    # and not including itself!

    if g.out_degree(current) == 0:
        memo[current] = 0
        return memo

    # Recursively subdivide the problem
    # amongst all the non-parent children.

    for c in g.neighbors(current):
        if c != parent:
            helper(g, memo, start, c, current)

    # Assume the problem is solved for children.
    # Collect and combine the results from
    # children for this step!

    # Define how to combine the results
    # assuming `memo[c]` contains the
    # number of bags fully contained in a
    # bag of color represented by node c.

    memo[current] = 0

    # For all the children, `c`,
    # `c` contributes some number of bags
    # that are fully contained in it
    # a total of the edge-weight times.

    # Next, we include the number of copies
    # of `c` in our `current` bag that now fully
    # contains all its children's bags.

    for c in g.neighbors(current):
        if c != parent:
            memo[current] += (1 + memo[c]) * g[current][c]["weight"]
    return memo


def process_group(grp):
    """
    Given a list of list of
    information about which bag
    contains which other bags,
    compute the total number of
    bags contained in a 'shiny gold'
    bag.

    :param grp: The list of list of
    information about the containment
    relationship of bags.

    :return: The total number of bags
    contained in a 'shiny gold' bag.

    """

    # Show a contains relationship.
    edges = []

    for i in range(len(grp)):
        node, *rest = grp[i].split(" bags contain ")
        bags = "".join(map(str, rest)).split(", ")
        for bag in bags:
            if bag == "no other bags.":
                continue
            bag_count, bag_first, bag_last, _ = bag.split(" ")
            bag_name = bag_first + " " + bag_last
            edges.append((node, bag_name, {"weight": int(bag_count)}))

    # Create a DiGraph.
    g = nx.DiGraph(edges)

    memo = dict()
    _target = "shiny gold"
    parent = "-1"

    # Compute the number of bags that _target contains.
    mm = helper(g, memo, _target, _target, parent)

    return mm[_target]


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
