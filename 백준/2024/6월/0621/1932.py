n = int(input())
arr = [[int(input())]]
dp = [arr[0]]

for i in range(2, n+1):
    arr.append(list(map(int, input().split())))
    dp.append([0] * i)

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + arr[i][j]

print(max(dp[n-1]))