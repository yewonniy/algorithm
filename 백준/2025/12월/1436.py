n = int(input()) # 정확히 n 키로 배달
max = 10**9
dp = [max] * (n+1)
dp[0] = 0
for i in range(n+1):
    if i-3 >= 0 and dp[i-3] >= 0:
        dp[i] = min(dp[i], dp[i-3]+1)
    if i-5 >= 0 and dp[i-5] >= 0:
        dp[i] = min(dp[i], dp[i-5]+1)

if dp[n] == max:
    print(-1)
else:
    print(dp[n])