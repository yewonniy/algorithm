n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]  # [무게, 가치]
arr.sort(key=lambda x:x[0])

dp = [[0]*(k+1) for _ in range(n)]

for i in range(n):
    w, value = arr[i]
    for j in range(k+1):
        if i == 0 and w <= j:
            dp[i][j] = value
        elif j < w:
            dp[i][j] = dp[i-1][j]
        elif j >= w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+value)

print(dp[n-1][k])
