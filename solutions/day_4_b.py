"""
My solution for the Problem 2 on
Day 4 of Advent of Code 2020.
"""

import re


def solve(_n, arr):
    """
    Given a list of list of "passports"
    separated by newlines, count
    the number of valid tokens
    where a token is said to be valid
    if and only if the keys in the tokens
    are either equal to a given set of keys
    or is missing a given key.

    :return: The number of valid passports.
    """

    fields = {
        "byr": (1920, 2002),
        "iyr": (2010, 2020),
        "eyr": (2020, 2030),
        "hgt": {"cm": (150, 193), "in": (59, 76)},
        "hcl": "^#[a-f0-9]{6}$",
        "ecl": {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        "pid": "^[0-9]{9}$",
        "cid": "",
    }

    def valid(keyMap):
        """
        Given a dictionary keyMap, determine
        if it satisfies the conditions defined
        in "fields".

        :return: True if keyMap is valid, False
        otherwise.
        """
        # Check that all required keys are present.
        present = set(fields) == set(keyMap)
        present = present or set(fields) == set(keyMap) | {"cid"}

        if not present:
            return False

        # Check the year bounds.
        for k in ("byr", "iyr", "eyr"):
            low, high = fields[k]
            if len(keyMap[k]) != 4 or not (low <= int(keyMap[k]) <= high):
                return False

        # Check the 'hgt' property.
        ht = keyMap["hgt"]
        if not ht.endswith("in") and not ht.endswith("cm"):
            return False
        else:
            val = int(ht[:-2])
            low, high = fields["hgt"][ht[-2:]]
            if not (low <= val <= high):
                return False

        # Check hcl and pid by matching regex.
        for k in ("hcl", "pid"):
            regex = fields[k]
            if not re.search(regex, keyMap[k]):
                return False
        # If it reaches here, then all else
        # is fine.

        # Check if 'ecl' is one of fields['ecl'].
        return keyMap["ecl"] in fields["ecl"]

    i = 0
    count = 0

    tokens = dict()

    while i < _n:
        if arr[i] == "" or i == _n:
            if valid(tokens):
                count += 1
            tokens = dict()
        else:
            ln = arr[i].split(" ")
            for pair in ln:
                k, v = pair.split(":")
                tokens[k] = v
        i += 1

    return count


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.

    Example
    ______

    _n = int(input())
    arr = []
    for _ in range(_n):
        arr.append(int(input()))
    result = solve(arr)

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
