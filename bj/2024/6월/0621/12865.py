n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (k+1)

valid = 0
for i in range(n):
    if arr[i][0] <= k:
        valid = 1
if valid == 0:
    print(0)
else:
    for i in range(n):
        weight = arr[i][0]
        value = arr[i][1]
        if weight <= k:
            check = [False] * (k+1)
            if value > dp[weight]:
                dp[weight] = value
                check[weight] = True
            for j in range(k+1):
                if j - weight > 0 and not check[j - weight]:
                    if dp[j - weight] + value > dp[j]:
                        dp[j] = dp[j - weight] + value
                        check[j] = True
    print(max(dp))