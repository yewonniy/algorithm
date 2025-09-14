n = int(input())
arr = [0] * (n+1)
arr[1] = 1
arr[2] = 2
for i in range(3, n+1):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[n])


def dp(n):
    if memo[n] != 0:
        return memo[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    memo[n] = dp(n-1) + dp(n-2)
    return memo[n]


memo = [0] * (n+1)
res = dp(n)
print(res)