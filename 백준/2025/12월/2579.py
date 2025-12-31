n = int(input())
arr = [int(input()) for _ in range(n)]
arr = arr[::-1]


def cal():
    if n == 1:
        return arr[0]
    elif n == 2:
        return sum(arr)
    dp = [[0, 0] for _ in range(n)]
    dp[0][0], dp[0][1] = arr[0],arr[0]
    dp[1][0], dp[1][1] = arr[0]+arr[1], arr[0]
    dp[2][0], dp[2][1] = arr[0]+arr[2], dp[1][0]

    for i in range(3, n):
        dp[i][0] = arr[i] + max(dp[i-1][1], dp[i-2][1] + arr[i-1]) # i 밟기 = max(i-2밟기, i-1밟기)
        dp[i][1] = dp[i-1][0] # i 안밟기 = i-1 밟은 값

    return max(dp[n-1])


print(cal())