def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.
    >>> race(5, 7) # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
        print(tortoise, hare, minutes)
    return minutes


def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0: print("fizzbuzz")
        elif i % 3 == 0: print("fizz")
        elif i % 5 == 0: print("buzz")
        else :print(i)


def isPrime(n):
    i = 2
    if n == 1: return False
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True


def uniqueDigits(n):
    """
    Return the number of unique digits in positive integer n.
    >>> uniqueDigits(8675309) # All are unique
    7
    >>> uniqueDigits(13173131) # 1, 3, and 7
    3
    >>> uniqueDigits(101) # 0 and 1
    2
    """

    res = 0
    for i in range(0, 10):
        k = n
        while k > 0:
            if k % 10 == i: 
                res += 1
                break
            k //= 10
    return res
