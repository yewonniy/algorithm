# 1차원 배열 사용시 -> 뒤부터 순환
# 2차원 배열 사용시 -> 앞부터 순환
# 2차원 배열을 사용해 볼게
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n)]

for i in range(n):
    weight = arr[i][0]
    value = arr[i][1]
    for j in range(k+1):
        if j >= weight:
            if i == 0:
                dp[i][j] = value
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)  # dp[i-1][j-weight]에 value를 더하는 게 포인트!!!
        else:
            if dp[i-1][j] > 0:
                dp[i][j] = dp[i-1][j]

print(max(dp[n-1]))


# 4 7
# 6 13
# 4 8
# 3 6
# 5 12