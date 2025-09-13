import sys
sys.setrecursionlimit(20000)
n = int(input())
arr = []
s = set()
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
    for x in a:
        s.add(x)
standard = sorted(list(s))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def rain(t):
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= t:
                arr[i][j] = 0
                visited[i][j] = True


def start():
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                return [i, j]
    return [-1, -1]


def dfs(a, b):
    global cnt
    visited[a][b] = True
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < n and not visited[x][y]:
            dfs(x, y)


res = 0
for i in standard:
    visited = list([False] * n for _ in range(n))
    cnt = 0
    while True:
        rain(i)
        x, y = start()
        if x == -1 and y == -1:
            break
        dfs(x, y)
        cnt += 1
    res = max(res, cnt)
print(res)