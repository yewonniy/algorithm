N = int(input())

def factorial(num, N):
    if num == N:
        mul = 1
    mul = mul*num
    if num > 1:
        num = num-1
        factorial(num, N-1)
    else:
        return mul

factorial_n = factorial(N, N)
