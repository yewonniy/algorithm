from collections import deque
import sys
# bfs
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(a, b, m, n):
    q = deque()
    q.append([a,b])
    graph[a][b] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0<=xx<n and 0<=yy<m and graph[xx][yy] == 1:
                graph[xx][yy] = 0
                q.append([xx, yy])


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    arr = []
    for _ in range(k):
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
        arr.append([x,y])
    cnt = 0
    for x, y in arr:
        if graph[x][y] == 1:
            bfs(x, y, m , n)
            cnt += 1
    print(cnt)