from collections import deque
n = int(input())
arr = [list(map(int, list(input()))) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]


def bfs(a, b):
    q = deque()
    q.append((a,b))
    arr[a][b] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0<=xx<n and 0<=yy<n and arr[xx][yy]==1:
                arr[xx][yy] = 0
                q.append((xx, yy))
                cnt += 1
    return cnt


res = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            res.append(bfs(i, j))
res.sort()
print(len(res))
for x in res:
    print(x)