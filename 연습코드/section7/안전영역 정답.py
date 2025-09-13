import sys
sys.setrecursionlimit(20000)
n = int(input())
board = []
s = set()
for i in range(n):
    a = list(map(int, input().split()))
    board.append(a)
    for x in a:
        s.add(x)
standard = sorted(list(s))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y, h):
    visited[x][y] = True
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy] and board[xx][yy] > h:
            DFS(xx, yy, h)


cnt = 0
res = 0
for h in standard:
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] > h:
                cnt += 1
                DFS(i, j, h)
    res = max(res, cnt)
print(res)