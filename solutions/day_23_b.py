"""
My solution for the Problem 2 on
Day 23 of Advent of Code 2020.
"""

from functools import reduce
import operator


class LinkedNode:
    """
    A class to represent
    nodes of a linked list.
    """

    def __init__(self, value: int, nxt=None):
        """
        A linked node has a value and a reference
        to the next node.
        """
        self.value = value
        self.nxt = nxt

    def __str__(self):
        """
        A str representation
        sometimes useful for debugging.
        """
        if self.nxt:
            return f"value: {str(self.value)}  -->  next: {str(self.nxt.value)}"
        return f"value: {str(self.value)} -->  next: None"


def play(ll, head: LinkedNode):
    """
    Given a dict of linkedNodes
    and a reference to its head,
    simulate the game play of Day 23.
    :param ll: A dict with keys as ints,
    and values as LinkedNodes.
    :param head: A LinkedNode already
    present in the dict.
    """
    for _ in range(10_000_000):
        # The current element under
        # consideration is head.value.

        # Extract the triple of values.
        triple_start = head.nxt
        triple_end = head.nxt.nxt.nxt
        triple_values = [triple_start.value, head.nxt.nxt.value, triple_end.value]

        dest = head.value - 1
        if dest <= 0:
            dest = 1_000_000
        while dest in triple_values:
            dest -= 1
            if dest == 0:
                dest = 1_000_000

        # The next element to consider
        # is after the triple.
        head.nxt = triple_end.nxt

        # Insert the whole triple
        # between ll[dest] and ll[dest].nxt
        triple_end.nxt = ll[dest].nxt
        ll[dest].nxt = triple_start

        # Update the head to its neighbor.
        head = head.nxt
    return


def process_group(grp):
    """
    See AoC Day 23.
    :param grp: A string of digits
    0-9 occurring at most once.

    :return: An int, the product of
    the two successive neighbors of
    1 after the game ends.
    """

    arr = list(map(int, list(grp[0])))
    ll = dict()
    # Create all nodes.
    for i in range(1, 1_000_001):
        ll[i] = LinkedNode(i)

    # Join the nodes from the given input.
    for i in range(len(arr) - 1):
        ll[arr[i]].nxt = ll[arr[i + 1]]

    # Join the last entry of the array to node
    # with label 10.
    ll[arr[-1]].nxt = ll[10]

    # Join the rest of million nodes together.
    for i in range(10, 1_000_000):
        ll[i].nxt = ll[i + 1]

    # Join the last node to the first one.
    ll[1_000_000].nxt = ll[arr[0]]

    # Simulate the crab game.
    play(ll, ll[arr[0]])

    # Return the product of values of successive neighbors of 1.
    return ll[1].nxt.value * ll[1].nxt.nxt.value


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
