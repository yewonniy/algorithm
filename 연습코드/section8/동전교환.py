n = int(input())
arr = list(map(int, input().split()))
m = int(input())
memo = list([99999999] * (m+1) for _ in range(n))
memo[0][0] = 0

for i in range(m+1):
    coin = arr[0]
    if i % coin == 0:
        memo[0][i] = i // coin

for i in range(1, n):
    for j in range(m+1):
        if j-arr[i] >= 0:
            memo[i][j] = min(memo[i-1][j-arr[i]] + 1, memo[i][j-arr[i]] + 1, memo[i-1][j])
        else:
            memo[i][j] = memo[i-1][j]
print(memo[-1][-1])