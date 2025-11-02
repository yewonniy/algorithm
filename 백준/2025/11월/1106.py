c, n = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split()))) # 금액, 고객
dp = [[0] * (c+1) for _ in range(n)]

for i in range(n):
    cost, customer = arr[i]
    for j in range(1, c+1):
        mod = 1
        if j % customer == 0:
            mod = 0
        if i == 0:
            dp[i][j] = (j//customer + mod) * cost
        else:
            if j-customer >= 0:
                dp[i][j] = min(dp[i-1][j], (j//customer + mod) * cost, dp[i][j-customer] + cost)
            else:
                dp[i][j] = min(dp[i - 1][j], (j // customer + mod) * cost)
print(dp[n-1][c])
