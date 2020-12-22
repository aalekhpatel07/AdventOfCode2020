"""
My solution for the Problem 1 on
Day 20 of Advent of Code 2020.
"""

from functools import reduce
from itertools import product
from copy import deepcopy as dc


def get_right_strip(chonk):
    """
    Compute the right vertical strip of a 2D list.
    """
    return [chonk[_i][-1] for _i in range(len(chonk))]


def get_top_strip(chonk):
    """
    Compute the top horizontal strip of a 2D list.
    """
    return chonk[0]


def get_left_strip(chonk):
    """
    Compute the left vertical strip of a 2D list.
    """
    return [chonk[_i][0] for _i in range(len(chonk))]


def get_bottom_strip(chonk):
    """
    Compute the bottom horizontal strip of a 2D list.
    """
    return chonk[-1]


def get_chonk(whole, i, j, n=12):
    """
    Given an index (i, j)
    return a sublist of size 10 x 10
    from the "whole" list.

    """
    block_size = 10

    res = [[None for _ in range(block_size)] for _ in range(block_size)]

    for x in range(block_size):
        for y in range(block_size):
            res[x][y] = whole[block_size * i + x][block_size * j + y]
    return res


def fits(whole, chunk, i, j, n=12):
    """
    Determine if the given chunk fits at
    block (i, j) in the "whole" 2D list.

    :return: True if its borders align
    with its neighbors' borders, False otherwise.

    """
    _empty = ["." for _ in range(10)]
    if i == 0:
        if j == 0:
            rs = get_right_strip(chunk)
            bs = get_bottom_strip(chunk)

            right_nb_left = get_left_strip(get_chonk(whole, 0, 1, n))
            bottom_nb_top = get_top_strip(get_chonk(whole, 1, 0, n))

            return all(
                [
                    right_nb_left == _empty or right_nb_left == rs,
                    bottom_nb_top == _empty or bottom_nb_top == bs,
                ]
            )
        elif 0 < j < n - 1:
            rs = get_right_strip(chunk)
            bs = get_bottom_strip(chunk)
            ls = get_left_strip(chunk)

            right_nb_left = get_left_strip(get_chonk(whole, 0, j + 1, n))
            bottom_nb_top = get_top_strip(get_chonk(whole, 1, j, n))
            left_nb_right = get_right_strip(get_chonk(whole, 0, j - 1, n))

            return all(
                [
                    right_nb_left == _empty or right_nb_left == rs,
                    bottom_nb_top == _empty or bottom_nb_top == bs,
                    left_nb_right == _empty or left_nb_right == ls,
                ]
            )

        elif j == n - 1:
            bs = get_bottom_strip(chunk)
            ls = get_left_strip(chunk)

            left_nb_right = get_right_strip(get_chonk(whole, 0, n - 2, n))
            bottom_nb_top = get_top_strip(get_chonk(whole, 1, n - 1, n))

            return all(
                [
                    bottom_nb_top == _empty or bottom_nb_top == bs,
                    left_nb_right == _empty or left_nb_right == ls,
                ]
            )
    elif 0 < i < n - 1:
        if j == 0:
            rs = get_right_strip(chunk)
            ts = get_top_strip(chunk)
            bs = get_bottom_strip(chunk)

            bottom_nb_top = get_top_strip(get_chonk(whole, i + 1, 0, n))
            top_nb_bottom = get_bottom_strip(get_chonk(whole, i - 1, 0, n))
            right_nb_left = get_left_strip(get_chonk(whole, i, 1, n))

            return all(
                [
                    bottom_nb_top == _empty or bottom_nb_top == bs,
                    top_nb_bottom == _empty or top_nb_bottom == ts,
                    right_nb_left == _empty or right_nb_left == rs,
                ]
            )
        elif 0 < j < n - 1:

            rs = get_right_strip(chunk)
            ts = get_top_strip(chunk)
            bs = get_bottom_strip(chunk)
            ls = get_left_strip(chunk)

            bottom_nb_top = get_top_strip(get_chonk(whole, i + 1, j, n))
            top_nb_bottom = get_bottom_strip(get_chonk(whole, i - 1, j, n))
            right_nb_left = get_left_strip(get_chonk(whole, i, j + 1, n))
            left_nb_right = get_right_strip(get_chonk(whole, i, j - 1, n))

            return all(
                [
                    bottom_nb_top == _empty or bottom_nb_top == bs,
                    top_nb_bottom == _empty or top_nb_bottom == ts,
                    right_nb_left == _empty or right_nb_left == rs,
                    left_nb_right == _empty or left_nb_right == ls,
                ]
            )
        elif j == n - 1:
            ts = get_top_strip(chunk)
            bs = get_bottom_strip(chunk)
            ls = get_left_strip(chunk)

            bottom_nb_top = get_top_strip(get_chonk(whole, i + 1, j, n))
            top_nb_bottom = get_bottom_strip(get_chonk(whole, i - 1, j, n))
            left_nb_right = get_right_strip(get_chonk(whole, i, j - 1, n))

            return all(
                [
                    bottom_nb_top == _empty or bottom_nb_top == bs,
                    top_nb_bottom == _empty or top_nb_bottom == ts,
                    left_nb_right == _empty or left_nb_right == ls,
                ]
            )
    elif i == n - 1:
        if j == 0:
            rs = get_right_strip(chunk)
            ts = get_top_strip(chunk)

            top_nb_bottom = get_bottom_strip(get_chonk(whole, i - 1, j, n))
            right_nb_left = get_left_strip(get_chonk(whole, i, j + 1, n))

            return all(
                [
                    top_nb_bottom == _empty or top_nb_bottom == ts,
                    right_nb_left == _empty or right_nb_left == rs,
                ]
            )
            pass
        elif 0 < j < n - 1:
            rs = get_right_strip(chunk)
            ts = get_top_strip(chunk)
            ls = get_left_strip(chunk)

            top_nb_bottom = get_bottom_strip(get_chonk(whole, i - 1, j, n))
            right_nb_left = get_left_strip(get_chonk(whole, i, j + 1, n))
            left_nb_right = get_right_strip(get_chonk(whole, i, j - 1, n))

            return all(
                [
                    top_nb_bottom == _empty or top_nb_bottom == ts,
                    right_nb_left == _empty or right_nb_left == rs,
                    left_nb_right == _empty or left_nb_right == ls,
                ]
            )
            pass
        elif j == n - 1:
            ts = get_top_strip(chunk)
            ls = get_left_strip(chunk)

            top_nb_bottom = get_bottom_strip(get_chonk(whole, i - 1, j, n))
            left_nb_right = get_right_strip(get_chonk(whole, i, j - 1, n))

            return all(
                [
                    top_nb_bottom == _empty or top_nb_bottom == ts,
                    left_nb_right == _empty or left_nb_right == ls,
                ]
            )

    return False


def empty_chunk(n):
    """
    Produce a 2D list
    of size n x n that
    is populated with ".".
    """
    return [["." for _ in range(n)] for _ in range(n)]


def dfs(whole, row_idx, col_idx, n, tiles_assigned, mappings, used):
    """
    DP the whole grid in the order left-to-right and top-to-bottom.
    Where possible, place a tile, and if the end is reached,
    we have a valid solution, otherwise it fails at some point
    and then backtracks to a previous state.

    :return: True if a valid tile assignment exists,
    False otherwise.

    Notes
    _____

    The "tiles_assigned" list is populated
    if a solution is found. So we can inspect that
    after this function finishes executing.

    """

    # Reached the terminal state.
    if row_idx == n - 1 and col_idx == n:
        return True

    # Hit the end of row. Go to next row and first column.
    elif col_idx == n:
        return dfs(whole, row_idx + 1, 0, n, tiles_assigned, mappings, used)
    else:
        # Check which tile id should fit at block (row_idx, col_idx).
        for k in mappings:
            # Only worry about unused tiles,
            # since we can use a tile only once.
            if k not in used:
                for tile in mappings[k]:
                    # If the tile fits fine:
                    if fits(whole, tile, row_idx, col_idx, n):
                        # Place it.
                        whole = chunk_replace(whole, row_idx, col_idx, dc(tile))
                        # Record the id of the tile at that index.
                        tiles_assigned[row_idx][col_idx] = k
                        if dfs(
                            whole,
                            row_idx,
                            col_idx + 1,
                            n,
                            tiles_assigned,
                            mappings,
                            used | {k},
                        ):
                            # This means, a valid assignment was found.
                            return True
                        # Somewhere down the line, an index had no
                        # good candidates for tiles. It made
                        # the tile assignment bad.
                        # So correct that by backtracking.

                        else:
                            # Reset the tile assignment.
                            tiles_assigned[row_idx][col_idx] = -1
                            # Replace the block with '.'.
                            whole = chunk_replace(
                                whole, row_idx, col_idx, empty_chunk(10)
                            )
        # All keys were used but no matching tile was found for this
        # index, so return False.
        return False


def pp(*tables):
    """
    A helper method
    to simply print multiple
    chunks of "." and "#" side-by-side.
    """
    res = ""
    for zipped_row in zip(*tables):
        res += "\t".join(tuple("".join(x) for x in zipped_row)) + "\n"
    print(res)


def parse_images(grp):
    """
    Read the input data into titles and
    images.
    """
    images = []
    titles = []

    for i in range(len(grp) // 11):
        _title = int(grp[11 * i][:-1].split(" ")[1])
        titles.append(_title)
        images.append(grp[11 * i + 1 : 11 * (i + 1)])
    return titles, images


def solve(grp):
    """
    """
    from math import sqrt

    res = get_all_transforms(*parse_images(grp))
    _boxes = len(res)
    _sz = int(sqrt(_boxes))
    canvas = [["." for _ in range(_sz * 10)] for _ in range(_sz * 10)]
    used = set()
    tiles_assigned = [[-1 for _ in range(_sz)] for _ in range(_sz)]
    dfs(canvas, 0, 0, _sz, tiles_assigned, res, used)
    return (
        tiles_assigned[0][0]
        * tiles_assigned[0][-1]
        * tiles_assigned[-1][-1]
        * tiles_assigned[-1][0]
    )


def get_all_transforms(titles, data):
    """
    Given a list of titles and
    tile data associated to each title,
    compute a dictionary that has as keys
    the unique titles and as values, a
    list of rotations and flips of each tile
    that is associated to each title.

    :param titles: A list of tile ids.

    :param data: A list of 2D lists that
    represent blocks in the data.

    :return: A dictionary of tile ids and
    its corresponding collection of flips
    and rotations.

    """
    res = dict()

    for title, d in zip(titles, data):
        res[title] = transform(d)
    return res


def transform(arr):
    """
    Given a 2D list,
    rotate and flip it in
    all possible ways and return
    a collection of the views after
    simulating such flips and
    rotations.

    :param arr: A 2D list
    :return: A list of rotations
    and flips of arr.

    """
    # One flip and 4 rotations.
    res = []
    curr = dc([list(x) for x in arr])
    res.append(curr)

    for _ in range(3):
        curr = rotate_right(curr)
        res.append(dc(curr))

    curr = flip_transpose(arr)

    for _ in range(4):
        curr = rotate_right(curr)
        res.append(dc(curr))

    return res


def rotate_right(arr):
    """
    Rotate a copy of given 2D list
    clockwise by 90 degrees
    and return a new list.

    :param arr: A 2D-list of arbitrary
    dimensions.

    :return: A list that is "arr" rotated
    90 degree clockwise by its center.
    """
    n = len(arr)
    m = len(arr[0])

    res = [[None for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j] = arr[n - j - 1][i]

    return res


def flip_transpose(arr):
    """
    Flip a 2D-list (i.e. transpose).
    """
    m = len(arr)
    n = len(arr[0])
    res = [[-1 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            res[i][j] = arr[j][i]
    return res


def chunk_replace(block, i, j, chunk):
    """
    Replace the chunk of size 10 x 10
    corresponding to a sublist indexed
    by (i, j) in the larger list "block".
    """
    temp = dc(block)
    for x in range(len(chunk)):
        for y in range(len(chunk)):
            temp[10 * i + x][10 * j + y] = chunk[x][y]
    return temp


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
