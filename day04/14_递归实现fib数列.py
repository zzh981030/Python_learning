def fib(n):
    """fib数列"""
    if n == 1 or n == 2:
        return  1
    return  fib(n-1) + fib(n-2)

# 1, 1, 2, 3, 5, 8
print(fib(5))