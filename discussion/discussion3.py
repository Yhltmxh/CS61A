

def swipe(n):
    """
    Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """

    if n == 0: return
    print(n % 10)
    swipe(n // 10)
    if n // 10 > 0: print(n % 10)


def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...
    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 0: return 1
    return n * skip_factorial(n - 2)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """

    def check(i):
        if i == n:
            return True
        elif n % i == 0:
            return False
        return check(i + 1)
    return check(2)


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n == 1: 
        return 1
    if n % 2 == 0: 
        return 1 + hailstone(n // 2)
    else: 
        return 1 + hailstone(n * 3 + 1)

# 循环写法
def sevens_for(n, k):
    cur, op = 1, 1
    for i in range(1, n + 1):
        print("Player {} says {}".format(cur, i))
        if i % 7 == 0 or has_seven(i): op = -op
        cur += op
        if cur > k: cur %= k
        elif cur == 0: cur = k
    return cur  


def has_seven(n):
    while n > 0:
        if n % 10 == 7: return True
        n //= 10
    return False


# 递归写法
def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.
    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """

    def f(x, cur, op):
        # print("Player {} says {}".format(cur, x))
        if x == n: return cur
        x += 1
        cur += op
        if cur > k: cur %= k
        elif cur == 0: cur = k
        if x % 7 == 0 or has_seven(x):
            op = -op
        return f(x, cur, op)
    return f(1, 1, 1)


