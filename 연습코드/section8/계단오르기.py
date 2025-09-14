n = int(input())
memo = [0] * (n+1)


def dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if memo[n] != 0:
        return memo[n]
    memo[n] = dp(n-1) + dp(n-2)
    return memo[n]


dp(n)
print(memo[n])