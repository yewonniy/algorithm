n, m = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n))
memo = [0] * (m+1)
for i in range(n):
    for j in range(m+1):
        if j-arr[i][0] >= 0:
            memo[j] = max(memo[j], arr[i][1] * (j//arr[i][0]), memo[j-arr[i][0]] + arr[i][1])
print(memo[-1])