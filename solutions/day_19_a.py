"""
My solution for the Problem i on
Day j of Advent of Code 2020.

This is a template that I'll be using
to solve problems.
"""

from functools import reduce
import operator
from itertools import product


def split(it, _f):
    res = []
    for elem in it:
        if not _f(elem):
            res.append(elem)
        else:
            yield res[:]
            res = []
    yield res


def parse_rules(rules):
    adj_list = list(map(lambda x: tuple(x.split(":")), rules))
    adj = dict()

    for v, rule_v in adj_list:
        adj[int(v)] = tuple(rule_v.split("|"))
    memo = dict()
    curr = 0
    for k in adj:
        temp = adj[k]
        chars = []
        for t in temp:
            if t.strip() == '"a"' or t.strip() == '"b"':
                chars.append(t.strip().replace('"', ""))
            else:
                chars.append(list(map(int, t.strip().split(" ")[:])))
        adj[k] = chars[:]

    _, memo = generate_rules(adj, curr, memo)

    # memo[0] = []
    # for group in adj[0]:
    #     for entries in product(*[memo[z] for z in group]):
    #         memo[0].append("".join(entries))
    return memo


def generate_rules(adj, curr, memo):
    if len(adj[curr]) == 1 and isinstance(adj[curr][0], str):
        memo[curr] = adj[curr]
        return memo[curr], memo
    elif curr in memo:
        return memo[curr], memo
    else:
        for group in adj[curr]:
            # print(curr, group)
            for entry in group:
                _, memo = generate_rules(adj, entry, memo)
        if curr not in memo:
            memo[curr] = []
        for group in adj[curr]:
            temp = [memo[z] for z in group]
            for cols in product(*temp):
                memo[curr].append("".join(cols))
    return _, memo


def solve(grp):
    """
    """

    def ssplit(it, _f):
        res = []
        for elem in it:
            if not _f(elem):
                res.append(elem)
            else:
                yield res[:]
                res = []
        yield res

    rules, strings = list(ssplit(grp, lambda x: x == ""))
    memo = parse_rules(rules)
    zero = memo[0]
    print("memo computing done!")
    print(0 in memo)
    print(len(memo[0]), len(strings))
    count = 0
    for m in strings:
        if any(x == m for x in zero):
            count += 1

    return count


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
