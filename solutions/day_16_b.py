"""
My solution for the Problem 2 on
Day 16 of Advent of Code 2020.
"""

from functools import reduce
import operator


def read_ranges(_a):
    """
    Given the block of text
    describing the fields and
    its valid ranges, parse the
    input and for every int in the
    valid ranges, record all the different
    fields that are valid for it.

    :param _a: The first block of text
    from AoC Day 16 input.

    :return: A dictionary with ints as keys
    and as values, the list of fields that contain
    the key in their range of valid input.

    """

    rngs = []
    for _row in range(len(_a)):
        field, *rest = _a[_row].split(": ")
        r1, r2 = "".join(rest).split(" or ")
        r1s, r1e = list(map(int, r1.split("-")))
        r2s, r2e = list(map(int, r2.split("-")))
        rngs += [(r1s, r1e, field), (r2s, r2e, field)]

    bound_end = max([(y, x) for x, y, field in rngs])
    bound_start = min(rngs)

    _lwr = bound_start[0]
    _upper = bound_end[0]

    result = {i: [] for i in range(_lwr, _upper + 1)}

    for _s, _e, _field in rngs:
        for _i in range(_s, _e + 1):

            result[_i].append(_field)

    return result


def perfect_matching(edges):
    """
    Given a set of edges, construct
    a bipartite graph and produce a
    perfect matching in it.

    :param edges: A list of tuples
    representing edges between two nodes.

    :return: A dictionary with keys as
    vertices and values as the unique
    vertex that it is paired with.

    """

    import networkx as nx
    from networkx.algorithms.bipartite.matching import hopcroft_karp_matching as hkm

    G = nx.Graph()
    G.add_edges_from(edges)

    return hkm(G)


def traverse_columns(grid, _map):
    """
    Given a grid of ints and a map,
    describing what fields does a value
    in the grid correspond to, form a bipartite
    graph with set A as the set of columns of the
    grid, and set B as the set of fields.

    :param grid: A 2D-grid of ints.
    :param _map: A dictionary with keys ints and values
    as a list of fields that it is valid for.

    :return edges: A set of tuples that represent
    edges in a bipartite graph with partite sets A and B
    where A is the set of indices of columns in grid and
    B is the set of distinct fields.

    """

    edges = set()
    _g = []

    # Transform a list of strings into a list of lists.
    for _rw in grid:
        _g.append(list(map(int, _rw.split(","))))

    # For every column index:
    for _pos in range(len(_g[0])):
        # Extract `column` entry from all rows.
        # i.e. the `_pos`th column of grid.
        col = [_g[_i][_pos] for _i in range(len(_g))]

        # For a given column, map its entries
        # to a collection of sets of fields.
        mp = map(lambda x: set(_map[x]), col)

        # Reduce the collection by intersecting.
        neighbors = reduce(lambda acc, x: acc & x, mp)

        # Only any fields in the intersection are potential
        # candidates to be assigned that column of the grid.

        # Record that edge in the bipartite graph.
        for _n in neighbors:
            edges |= {(_pos, _n)}
    return edges


def solve(arr):
    """
    Aaarghhh! Too weird to
    describe. Read AoC Day 16
    problem statement. This
    solves that problem.

    :param arr: The input for AoC Day 16.

    :return: A number that is the product
    of indices from `your ticket` that are
    assigned fields that start with `departure`.

    """
    _i = 0
    coll = []
    curr_block = []

    # Collect the input blocks.
    while _i < len(arr):
        if len(arr[_i]) == 0:
            coll.append(curr_block)
            curr_block = []
        else:
            curr_block.append(arr[_i])
        _i += 1

    coll.append(curr_block)

    # Read the ranges from the first block.
    rngs = read_ranges(coll[0])

    # Extract the nearby tickets from the third block.
    nrby_t = coll[2][1:]

    # Filter out the invalid tickets.
    invalid = set()
    for row_idx, row in enumerate(nrby_t):
        for elem in map(int, row.split(",")):
            if elem not in rngs or not rngs[elem]:
                invalid |= {row_idx}
                break

    valid = {i for i in range(len(nrby_t))} - invalid

    # Now that we have a clean grid, traverse the columns
    # and collect candidates for the field-index assignment
    # in the form of edges of a bipartite graph.

    edgs = traverse_columns([nrby_t[i] for i in valid], rngs)

    # Compute a perfect matching.
    # This assigns a unique field to every column index of your ticket.

    pm = perfect_matching(edgs)

    # Read my ticket from the second block.
    my_ticket = list(map(int, coll[1][-1].split(",")))

    answer = 1

    # Filter and reduce as required.

    for fld in pm:
        if str(fld).startswith("departure"):
            answer *= my_ticket[pm[fld]]

    return answer


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
