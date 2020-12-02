"""
My solution for the Problem 1 on
Day 2 of Advent of Code 2020.
"""


def solve(tokens):
    """
    Given a list of tokens where
    each token is subdivided into
    a frequency range, a character,
    and a string, count the total
    number of tokens that are valid
    where a token is valid if and only
    if the frequency of the character
    appearing in the given string lies
    in the given frequency range.

    :param tokens: A list of tokens.

    :return: The answer required.
    """

    valid = 0

    for line in tokens:
        freq, char, string = line.split(" ")
        actual_char = char[:-1]
        low, high = list(map(int, freq.split("-")))
        if low <= string.count(actual_char) <= high:
            valid += 1

    return valid


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
