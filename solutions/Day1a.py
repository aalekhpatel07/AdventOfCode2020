def solve(arr):
    """
    Given an array of positive ints,
    find the product of two numbers that
    sum to 2020.

    :return: The product of the only two
             numbers in arr that sum to 2020.
    """
    s = set(arr)
    for i in s:
        if (2020 - i) in s:
            return i * (2020 - i)

    return 0


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    # a, b = list(map(int, input().split(' ')))
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    result = solve(arr)
    print(result)
    return result


def main():
    return driver()


if __name__ == '__main__':
    main()
