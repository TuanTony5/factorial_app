# Factorial function
def fact(n: int):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)
