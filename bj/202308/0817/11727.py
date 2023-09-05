n = int(input())

fact = [0] * 1000


def factorial(x):
    result = 1
    if fact[x] == 0:
        for num in range(x, 0, -1):
            result = result * num
        fact[x] = result
    return fact[x]


cnt = 1
for i in range(n//2 + 1, 0, -1):
    if 2 * i < n:
        j = n - 2 * i
        cnt += (factorial(i+j) // (factorial(i)*factorial(j)))*(2**i)
    elif 2 * i == n:
        cnt += 2**i

print(cnt % 10007)