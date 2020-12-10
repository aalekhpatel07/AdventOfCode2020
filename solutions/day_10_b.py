"""
My solution for the Problem 2 on
Day 10 of Advent of Code 2020.
"""

from functools import reduce
import operator


def process_group(grp):
    """
    Given a list of list of ints,
    where two ints share a directed edge
    u-v with v > u if v = u + i for some
    i in (1, 2, 3), compute the total number
    of branches (or equivalently leaves) in
    this directed tree.

    :param grp: The list of list of ints.
    :return: The count of the number of leaves.

    """

    st = list(sorted(map(int, grp)))
    st = [0] + st + [max(st) + 3]
    exists = set(st)

    def count_leaves(memo, curr_val):
        """
        Given a tree structure with root 0
        count the number of leaves present in it.

        Notes
        _____

        Recursive Step:

        Given a curr_val, we store in memo[curr_val]:

        'The number of leaves in the subtree rooted at curr_val.'

        """
        if curr_val == st[-1]:
            # Reached a leaf.

            # Leaves have exactly one leaf in the subtree
            # rooted at them.

            memo[curr_val] = 1
            return 1

        elif curr_val in memo:
            # If memoized, don't recompute, save time.
            return memo[curr_val]

        else:
            # Subdivide the problem amongst
            # the current nodes children.
            for i in range(1, 4):
                if curr_val + i in exists:
                    count_leaves(memo, curr_val + i)

            # Assume it is solved for children.

            # Then how to use children's solution
            # to produce current node's?

            # The number of leaves in the subtree rooted
            # at curr_val is:

            # The sum of the number of leaves in the
            # subtrees rooted at its children.

            memo[curr_val] = 0

            for i in range(1, 4):
                if curr_val + i in memo:
                    memo[curr_val] += memo[curr_val + i]

            # Populate memo[curr_val] with the result.
            # and trace back to the next node.

            return memo[curr_val]

    mm = dict()

    count_leaves(mm, 0)

    return mm[0]


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

    :param: The list of list.
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
