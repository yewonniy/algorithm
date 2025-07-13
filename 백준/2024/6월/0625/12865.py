n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
dy = [[0] * (k+1) for _ in range(n)]
for i in range(n):
    weight = arr[i][0]
    value = arr[i][1]
    for j in range(k+1):
        if j >= weight:
            if i == 0:
                dy[i][j] = value
            else:
                dy[i][j] = max(dy[i-1][j], dy[i-1][j-weight] + value)
        else:
            if dy[i-1][j] > 0:
                dy[i][j] = dy[i-1][j]
print(max(dy[n-1]))