n = int(input())
arr = []
for _ in range(n):
    r, g, b = map(int, input().split())
    arr.append([r, g, b])

memo = [[0, 0, 0] for _ in range(n)]
memo[0] = arr[0]

for i in range(1, n):
    for j in range(0,3):
        if j == 0:
            memo[i][j] = min(memo[i-1][1], memo[i-1][2]) + arr[i][j]
        elif j == 1:
            memo[i][j] = min(memo[i-1][0], memo[i-1][2]) + arr[i][j]
        else:
            memo[i][j] = min(memo[i-1][0], memo[i-1][1]) + arr[i][j]

print(min(memo[n-1]))