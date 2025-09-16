n, m = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n)) # 점수 시간
arr.sort(key=lambda x:x[1])
memo = list([0]*(m+1) for _ in range(n))

for i in range(m+1):
    if i >= arr[0][1]:
        memo[0][i] = arr[0][0]

for i in range(1, n):
    for j in range(m+1):
        if j-arr[i][1] >= 0:
            memo[i][j] = max(memo[i-1][j], memo[i-1][j-arr[i][1]] + arr[i][0])
        else:
            memo[i][j] = memo[i-1][j]
print(memo[-1][-1])