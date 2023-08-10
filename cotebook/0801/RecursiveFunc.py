def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
print(factorial(6))

def fibo_fuc(n):
    if n == 1 or n == 2:
        return 1
    return fibo_fuc(n-1) + fibo_fuc(n-2)
print(fibo_fuc(8))

