"""
My solution for the Problem 1 on
Day 22 of Advent of Code 2020.
"""


def solve(arr):
    """
    Given a list of str
    describing the decks
    that players begin with,
    simulate the game of
    combat.

    :param arr: A list of str
    representing the deck of cards.
    :return: An int, representing
    the winning player's score.
    """

    # Parse input.
    p1 = arr.index("Player 1:")
    p2 = arr.index("Player 2:")
    d1 = list(map(int, arr[p1 + 1 : p2]))
    d2 = list(map(int, arr[p2 + 1 :]))

    while d1 and d2:
        p1c = d1.pop(0)
        p2c = d2.pop(0)
        if p1c >= p2c:
            d1 += [p1c, p2c]
        else:
            d2 += [p2c, p1c]

    if d1:
        return sum(d1[-i - 1] * (i + 1) for i in range(len(d1)))
    return sum(d2[-i - 1] * (i + 1) for i in range(len(d2)))


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.

    """

    _n = int(input())
    arr = []
    for _ in range(_n):
        temp = input()
        if temp:
            arr.append(temp)

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
