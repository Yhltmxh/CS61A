

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    # def f(x, y):
    #     if x == m or y == n: return 1
    #     return f(x + 1, y) + f(x, y + 1)
    # return f(1, 1)
    if m == 1 or n == 1: return 1
    return paths(m - 1, n) + paths(m, n - 1)


def max_product(x):
    """Return the maximum product of non-consecutive elements of s.
    >>> max_product([10, 3, 1, 9, 2]) # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5]) # 5 * 5 * 5
    125
    >>> max_product([]) # The product of no numbers is 1
    1
    """
    if x == []: return 1
    elif len(x) == 1: return x[0]
    return max(x[0] * max_product(x[2:]), x[1] * max_product(x[3:]))


def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats.
    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    # if n < 0:
    #     return []
    # if n == 0:
    #     sums_to_zero = [] # The only way to sum to zero using positives
    #     return [sums_to_zero] # Return a list of all the ways to sum to zero
    # result = []
    # for k in range(1, m + 1):
    #     result = result + [[k] + rest for rest in sums(n-k, m) if rest == [] or rest[0] != k]
    # return result
    if n <= 0: return []
    elif n == 1: return [[1]]
    res = []
    for i in range(1, m + 1):
        for j in sums(n - i, m): 
            if i != j[0]: res.append([i] + j)
    if n <= m: res.append([n])
    return res
        