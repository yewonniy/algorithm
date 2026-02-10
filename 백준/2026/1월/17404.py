import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = float('inf')


def RGB(color_idx):
    global res
    dp = [[float('inf'), float('inf'), float('inf')] for _ in range(n)]  # dp[i][j] = i번째 집을 j색으로 칠하는 비용 (누적)
    # print("0번째 집을",color_idx,"번째 색으로 칠한다.")
    dp[0][color_idx] = arr[0][color_idx]
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]
    dp[n-1].pop(color_idx)
    res = min(res, min(dp[n-1]))


for i in range(3):
    RGB(i)
print(res)