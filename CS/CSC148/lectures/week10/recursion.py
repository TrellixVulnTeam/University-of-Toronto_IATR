# some recursive explorations
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
# import sys
# sys.setrecursionlimit(10**6)
from random import shuffle
from time import time


def fibonacci(n):
    """
    Return the nth fibonacci number, that is n if n < 2,
    or fibonacci(n-2) + fibonacci(n-1) otherwise.

    @param int n: a non-negative integer
    @rtype: int

    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(3)
    2
    """
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def fib_memo(n, seen):
    """
    Return the nth fibonacci number reasonably quickly.

    @param int n: index of fibonacci number
    @param dict[int, int] seen: already-seen results
    """
    if n not in seen:
        seen[n] = (n if n < 2
                   else fib_memo(n - 2, seen) + fib_memo(n - 1, seen))
    return seen[n]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    N = 30

    start = time()
    print(fib_memo(N, {}))
    print("Memoized Fibonacci run time: {}"
          .format(time() - start))

    start = time()
    print(fibonacci(N))
    print("Classic Fibonacci run time:  {}"
          .format(time() - start))
