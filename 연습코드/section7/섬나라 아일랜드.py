n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(a, b):
    arr[a][b] = 0
    for i in range(8):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < n and arr[x][y] == 1:
            dfs(x, y)


cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            dfs(i, j)
            cnt += 1
print(cnt)