arr = list(map(int, input().split()))  # [1, 2, 2, 4]

dp = [[[4 * len(arr) for _ in range(5)] for _ in range(5)] for _ in range(len(arr))]
dp[0][0][0] = 0


def move(a, b):
    if a == 0:
        return 2
    elif a == b:
        return 1
    elif abs(a-b) == 2:
        return 4
    else:
        return 3


for i in range(len(arr) - 1):
    target = arr[i]
    for left in range(5):
        for right in range(5):
            dp[i+1][left][target] = min(dp[i+1][left][target], dp[i][left][right] + move(right, target))  # 현재, 한칸 위 + 이동
            dp[i+1][target][right] = min(dp[i+1][target][right], dp[i][left][right] + move(left, target))
    print(dp[i+1])
print(min(map(min, dp[-1])))