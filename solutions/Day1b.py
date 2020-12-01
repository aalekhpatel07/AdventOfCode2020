def solve(arr):
    """
    Given an array of positive ints,
    find the product of three numbers that
    sum to 2020.

    :return: The product of the only three
             numbers in arr that sum to 2020.
    """

    s = dict()

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j]) in s:
                s[arr[i] + arr[j]] |= {(i, j)}
            else:
                s[arr[i] + arr[j]] = {(i, j)}


    for i in range(len(arr)):
        third = 2020 - arr[i]

        if third in s:
            for e_i, e_j in s[third]:
                if not(i in (e_i, e_j)):
                    return arr[i] * arr[e_i] * arr[e_j]

    return -1


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
