import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())
arr = []
q = deque()
non_ripe = 0
for z in range(h):
    tmp = []
    for x in range(n):
        tmp.append(list(map(int, input().split())))
        for y in range(m):
            if tmp[x][y] == 1:
                q.append((x,y,z))
            if tmp[x][y] == 0:
                non_ripe += 1
    arr.append(tmp)
# 탐색할 때는 arr[z][x][y] 순으로 검색
dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]


def bfs(cnt):
    res = 0
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            xx, yy, zz = x+dx[i], y+dy[i], z+dz[i]
            if 0 <= xx < n and 0 <= yy < m and 0 <= zz < h and arr[zz][xx][yy] == 0:
                arr[zz][xx][yy] = arr[z][x][y] + 1
                res = max(res, arr[zz][xx][yy])
                q.append((xx, yy, zz))
                cnt -= 1
    if cnt == 0:
        if res == 0:
            return 0
        return res-1
    return -1


print(bfs(non_ripe))