n, lim = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n))
arr.sort()
memo = list([0] * (lim+1) for _ in range(n))
res = [0] * lim

for i in range(lim+1):
    if i >= arr[0][0]:
        if i % arr[0][0] == 0:
            memo[0][i] = memo[0][i-1]+arr[0][1]
        else:
            memo[0][i] = memo[0][i-1]

for i in range(1,n):
    for j in range(lim+1):
        w = arr[i][0]
        v = arr[i][1]
        if j-w >= 0:
            memo[i][j] = max(memo[i][j-w] + v, memo[i-1][j-w] + v, memo[i-1][j])
        else:
            memo[i][j] = memo[i-1][j]
print(memo[-1][-1])
