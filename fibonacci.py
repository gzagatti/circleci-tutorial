def fib(n):
    if n <= 0 and round(n) != n:
        raise ValueError('n must be a positive integer and non-zero')
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
