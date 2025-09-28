n = int(input())
p = list(map(int, input().split()))

dp = [[float('-inf'), float('-inf')] for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    # j == 0: 지금까지 짝수 개 먹음
    dp[i+1][1] = max(dp[i+1][1], dp[i][0] + p[i])  # 이번에 먹으면 홀수번째, 키 더함
    # j == 1: 지금까지 홀수 개 먹음
    dp[i+1][0] = max(dp[i+1][0], dp[i][1] - p[i])  # 이번에 먹으면 짝수번째, 키 뺌
    # 그리고 먹지 않는 경우도 항상 고려
    for j in range(2):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])