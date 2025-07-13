n, k = map(int, input().split()) # 물건 수, 버틸 수 있는 무게
arr = [list(map(int, input().split())) for _ in range(n)] # 무게, 가치 순서
arr.sort()

dp = [[0] * (k+1) for _ in range(n)]

for i in range(n):
    for j in range(k+1):
        if i == 0 and j >= arr[i][0]:
            dp[i][j] = arr[i][1]
        elif i > 0:
            if j < arr[i][0]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i][0]] + arr[i][1])

print(dp[-1][-1])