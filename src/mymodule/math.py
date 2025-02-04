"""This do some math"""


def exponential(x, n):
    """Return x raised to the power of n"""
    return x**n


def factorial(n):
    """Return the factorial of n"""
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(exponential(2, 3) == 8)
    print(exponential(3, 0) == 1)
