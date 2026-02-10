import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]  # (무게, 가치)
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):  # i번째 물건을 넣어말아?
    w, v = arr[i-1]
    for j in range(k+1):  # 배낭 용량이 j 일때
        if w <= j:  # 배낭 용량이 내 물건 무게 이상이면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])