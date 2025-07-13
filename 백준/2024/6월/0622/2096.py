n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_dp = [0, 0, 0]
min_dp = [0, 0, 0]

for i in range(n):
    max_value0, max_value1, max_value2 = 0, 0, 0
    min_value0, min_value1, min_value2 = 10, 10, 10
    for j in range(3):
        if j == 0:
            max_value0 = max(max_dp[j], max_dp[j+1])
            min_value0 = min(min_dp[j], min_dp[j+1])
        elif j == 1:
            max_value1 = max(max_dp[j], max_dp[j-1], max_dp[j+1])
            min_value1 = min(min_dp[j], min_dp[j-1], min_dp[j+1])
        else:
            max_value2 = max(max_dp[j], max_dp[j-1])
            min_value2 = min(min_dp[j], min_dp[j-1])
    max_dp[0], max_dp[1], max_dp[2] = max_value0 + arr[i][0], max_value1 + arr[i][1], max_value2 + arr[i][2]
    min_dp[0], min_dp[1], min_dp[2] = min_value0 + arr[i][0], min_value1 + arr[i][1], min_value2 + arr[i][2]

print(max(max_dp), min(min_dp))