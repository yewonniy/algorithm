n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))
memo = list([99999999] * n for _ in range(n))
memo[0][0] = arr[0][0]

for i in range(n):
    for j in range(n):
        if i == 0 and j > 0:
            memo[i][j] = arr[i][j] + memo[i][j-1]
        if i > 0 and j == 0:
            memo[i][j] = arr[i][j] + memo[i-1][j]
        if i > 0 and j > 0:
            memo[i][j] = min(arr[i][j] + memo[i-1][j], arr[i][j] + memo[i][j-1])
print(memo[n-1][n-1])
print(memo)

memo = list([99999999] * n for _ in range(n))
memo[0][0] = arr[0][0]


def dp(x, y):
    if memo[x][y] != 99999999:
        return memo[x][y]
    if x == 0 and y == 0:
        return arr[0][0]
    elif y == 0:
        memo[x][y] = dp(x-1, y) + arr[x][y]
    elif x == 0:
        memo[x][y] = dp(x, y-1) + arr[x][y]
    else:
        memo[x][y] = min(dp(x-1, y), dp(x, y-1)) + arr[x][y]
    return memo[x][y]


dp(n-1, n-1)
print(memo)
print(memo[n-1][n-1])