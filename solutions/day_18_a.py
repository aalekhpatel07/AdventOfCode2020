"""
My solution for the Problem 1 on
Day 18 of Advent of Code 2020.
to solve problems.
"""

from functools import reduce
import operator


def parse(s):
    """
    Given a left-associative
    math expression involving
    only `+`, `*`, `(`, `)`,
    and usual numbers, parse
    the expression into a
    post-fix stack.

    :param s: A math expression
    in string form.

    :return st: A list representing
    a post-fix stack.

    """

    # Clean the string to read the brackets.
    s = s.replace("(", "( ").replace(")", " )")

    # Right-associativity implies usual order
    # but we need left-associativity
    # so parse it in reverse form.

    tokens = s.split(" ")[::-1]
    # For right associativity, use tokens[::-1].

    st, ops = [], []
    for idx, token in enumerate(tokens):
        if token == "(":

            # Collect all the operations after
            # previous expression ended.

            while ops[-1] != ")":
                st.append(ops.pop())

            # Remove the closing bracket.
            ops.pop()

        elif token == ")":
            ops.append(token)

        # If right-associative, use this
        # instead of above.

        # if token == ")":
        #   while ops[-1] != "(":
        #       st.append(ops.pop())
        #   ops.pop()

        # elif token == "(":
        #  ops.append(token)

        elif token == "+":
            ops.append(operator.add)
        elif token == "*":

            # For part b), collect
            # all recent adds
            # from ops into st
            # before appending mul.

            ops.append(operator.mul)
        else:
            st.append(int(token))

    while ops:
        st.append(ops.pop())
    return st


def evaluate(operations):
    """
    Given a post-fix expression
    in the form of a stack
    evaluate it.

    :param operations: A list representation
    of the postfix expression.

    :return: The result in the stack at the end.
    """
    res = []
    for idx, op in enumerate(operations):
        if isinstance(op, int):
            res.append(op)
        else:
            res.append(op(res.pop(), res.pop()))
    return res.pop()


def process_group(grp):
    """
    Given a list of math expressions
    involving `+`, `*`, `(`, `)`, and
    usual ints, evaluate every expression
    in a left-associative manner.

    :param grp: The list of math expressions.

    :return: The sum of the evaluation of all
    those expressions.

    """
    return reduce(operator.add, (evaluate(parse(s)) for s in grp))


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
