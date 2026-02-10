# 익기까지 며칠이 걸리는지, arr 행렬에 바로 저장
# arr[xx][yy] = arr[x][y] + 1
import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
arr = []
q = deque()
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))
    # 1은 익은 토마토, 0은 익지 않은 거, -1은 들어있지 않은 거


def if_ripe_all():
    res = 0
    for x in range(n):
        for y in range(m):
            res = max(res, arr[x][y])
            if arr[x][y] == 0:
                return -1
    return res-1


def bfs():
    # q에는 익은 토마토만 들어있음
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] == 0:
                arr[xx][yy] = arr[x][y] + 1
                q.append((xx, yy))
    return if_ripe_all()


print(bfs())
