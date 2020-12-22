"""
My solution for the Problem 2 on
Day 22 of Advent of Code 2020.
"""

from copy import deepcopy as dc
import sys


# Break the chains of stack!
sys.setrecursionlimit(7000)


def play(d1, d2, seen):
    """
    Simulate a recursive play
    described in AoC Day 22
    as recursive combat.

    :param d1: A list of ints
    representing cards of player 1.
    :param d2: A list of ints
    representing cards of player 2.
    :param seen: A set of tuples
    with two components: d1 and d2.

    :return: "p1" if Player 1 has won this round,
    "p2" otherwise.

    """

    # If the position is seen before:
    # player 1 wins.

    if (tuple(d1), tuple(d2)) in seen:
        return "p1", d1

    # If both decks have cards
    # then the game continues.

    if d1 and d2:
        seen |= {(tuple(d1), tuple(d2))}
        p1c = d1.pop(0)
        p2c = d2.pop(0)

        # Both players have enough cards
        # to play recursive combat.
        if len(d1) >= p1c and len(d2) >= p2c:
            next_p1 = dc(d1)[:p1c]
            next_p2 = dc(d2)[:p2c]
            new_seen = set()

            # Get the winner and winning deck
            # of recursive combat.
            winner, deck = play(next_p1, next_p2, new_seen)

            if winner == "p1":
                d1 += [p1c, p2c]
            else:
                d2 += [p2c, p1c]
        # At least one player does not have enough cards
        # to play recursive combat.
        else:
            if p1c >= p2c:
                d1 += [p1c, p2c]
            else:
                d2 += [p2c, p1c]
        # In this case, the game continues as usual.
        return play(d1, d2, seen)

    # Then the winner is decided!
    elif d1 and not d2:
        return "p1", d1
    elif d2 and not d1:
        return "p2", d2


def solve(arr):
    """
    Given a list of str
    describing the decks
    that players begin with,
    simulate the game of
    recursive combat.

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

    seen = set()
    # play the game.
    winner, deck = play(d1, d2, seen)
    return sum(deck[-i - 1] * (i + 1) for i in range(len(deck)))


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
