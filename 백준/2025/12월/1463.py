# dp
n = int(input())
dp = [float("INF")] * (n+2)
dp[1] = 0
# 1 to n
for i in range(1, n+1):
    dp[i+1] = min(dp[i+1], dp[i]+1) # +1 연산
    if i*2 < n+1:
        dp[i*2] = min(dp[i*2], dp[i]+1) # *2 연산
    if i*3 < n+1:
        dp[i*3] = min(dp[i*3], dp[i]+1) # *3 연산
print(dp[n])