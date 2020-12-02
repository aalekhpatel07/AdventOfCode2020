"""
My solution for the Problem 2 on
Day 2 of Advent of Code 2020.
This is a template that I'll be using
to solve problems.
"""


def solve(tokens):
    """
    Given a list of tokens,
    where each token is subdivided
    into three parts, an index (low, high),
    a char, and a string, count the number
    of valid tokens, where a token is
    defined to be valid if the character
    char occurs exactly at one of low/high
    in the given string.

    :param tokens: A list of tokens.

    :return: The count of valid tokens.
    """

    def check_char(idx, _c):
        return string[idx - 1] == _c

    valid = 0

    for line in tokens:
        indices, char, string = line.split(" ")
        low, high = list(map(int, indices.split("-")))
        cond = list(map(lambda x: check_char(x, char[:-1]), [low, high]))
        if any(cond) and not all(cond):
            valid += 1

    return valid


def driver():
    """
    Make sure this driver returns the result.

    :return: result - Result of computation.

    """

    _n = int(input())
    tokens = []
    for _ in range(_n):
        tokens.append(input())
    result = solve(tokens)
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
