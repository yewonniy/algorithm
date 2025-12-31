# bfs
from collections import deque
m, n = map(int, input().split())
target = m*n
graph = []
ripe = deque()
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(m):
        if arr[j] == 1:
            ripe.append((i,j))
        if arr[j] == -1:
            target -= 1
    graph.append(arr)
cnt_ripe = len(ripe)


def bfs(x, y):
    global cnt_ripe
    k = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if 0<=xx<n and 0<=yy<m:
            if graph[xx][yy] == 0:
                graph[xx][yy] = 1
                ripe.append((xx, yy))
                k += 1
    return k


def cal():
    res = 0
    global cnt_ripe
    while cnt_ripe < target:
        l = len(ripe)
        bfs_res = 0
        for _ in range(l):
            x,y = ripe.popleft()
            bfs_res += bfs(x, y)
        cnt_ripe += bfs_res
        res += 1
        if cnt_ripe == target:
            return res
        if bfs_res == 0:
            return -1
    return res


print(cal())