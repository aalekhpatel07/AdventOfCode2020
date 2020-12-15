"""
My solution for the Problem 2 on
Day 14 of Advent of Code 2020.
"""

from functools import reduce
import operator


def rpl_helper(_original, _replacement):
    """
    Given a list `_original`
    that contains '0', '1', or 'X',
    replace the occurrences of 'X'
    in `_original` with chronological
    values from `_replacement`.

    :param _original: A list of '0',
    '1' or 'X'.
    :param _replacement: A list of '0',
    or '1' that is of same length as the
    frequency of 'X' in _original.

    :return: A list of '0' or '1',
    where 'X's got replaced by corresponding
    entries of `_replacement`.

    """
    _result = []

    j = 0
    for i in range(len(_original)):
        if _original[i] == "X":
            _result.append(_replacement[j])
            j += 1
        else:
            _result.append(_original[i])
    return "".join(_result)


def _apply_mask(_m, _val):
    """
    Given a mask `_m` that is
    a string of 36 bits each '0',
    '1' or 'X', apply it to a given
    value.

    :param _m: The mask string
    :param _val: A value to be masked.

    :return: A set of all possible
    masked values.

    """

    v = str(bin(int(_val)))[2:]
    v = ["0"] * (36 - len(v)) + list(v)

    _idcs = set()

    for i in range(len(_m)):
        if _m[i] == "0":
            continue
        else:
            v[i] = _m[i]
            if _m[i] == "X":
                _idcs |= {i}

    if len(_idcs) == 0:
        return {int("".join(v), 2)}

    combs = set()

    for num in range(2 ** len(_idcs)):
        s = str(bin(num))[2:]
        s = ["0"] * (len(_idcs) - len(s)) + list(s)
        combs |= {rpl_helper(v, s)}

    return combs


def process_group(grp):
    """
    Given a list of list of tokens
    where each token is either `mask = XX0101X...`
    or `mem[address] = value`, simulate whatever
    day 14 has in its description.

    :param grp: The list of list of tokens.

    :return: The sum of all values left in memory
    after the process is simulated.
    """

    mask = ""
    space = dict()

    for _ins in grp:
        if _ins.startswith("mask"):
            mask = _ins.split(" = ")[1]
        else:
            mem, value = _ins.split(" = ")
            address = int(mem[4:-1])

            for _address in _apply_mask(mask, address):
                space[_address] = int(value)

    return sum(space.values())


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
