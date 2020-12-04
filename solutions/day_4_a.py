"""
My solution for the Problem 1 on
Day 4 of Advent of Code 2020.
"""


def solve(_n, arr):
    """

    Given a list of list of "passports"
    separated by newlines, count
    the number of valid tokens
    where a token is said to be valid
    if and only if the keys in the tokens
    are either equal to a given set of keys
    or is missing a given key.

    :return: The answer required.
    """
    fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}

    def valid(keys):
        """
        Given a list of keys
        determine if the list
        contains the same keys
        as fields or if it is missing
        at most one key "cid".

        :return: True if it is the same
        as fields or if it is missing the
        "cid" key; False otherwise.
        """
        return fields == set(keys) or fields == set(keys) | {"cid"}

    _i = 0
    count = 0

    tokens = []

    while _i < _n:
        if arr[_i] == "":
            if valid(tokens):
                count += 1
            tokens = []
        else:
            ln = arr[_i].split(" ")
            for pair in ln:
                _k, _v = pair.split(":")
                tokens.append(_k)
        _i += 1

    if valid(tokens):
        count += 1

    return count


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.

    """

    _n = int(input())
    arr = []

    for i in range(_n):
        arr.append(input())

    result = solve(_n, arr)
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
