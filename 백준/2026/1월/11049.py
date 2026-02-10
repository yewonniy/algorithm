import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for bunch in range(1, n): # 1 ~ n-1
    for i in range(n-bunch):
        j = i + bunch
        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+(arr[i][0] * arr[k][1] * arr[j][1]))
print(dp[0][n-1])