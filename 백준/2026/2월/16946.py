# 0 : 이동가능 1 : 벽
# 1. 모든 벽에 대해서 조사
# -> 해당 벽을 부순다면, 그 벽에서부터 이동할 수 있는 칸의 개수 (자신도 센다)
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split()) # 0 <= xx < n
arr = [list(map(int, (input().rstrip()))) for _ in range(n)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]
memo = dict()
key_store = [[0] * m for _ in range(n)]  # memo의 key값을 저장


def bfs(a, b):
    # arr[x][y]에서 출발해서 몇칸?
    # memo[x][y]
    can = []
    cnt = 1
    used = set()
    for i in range(4):
        xx, yy = a+dx[i], b+dy[i]
        if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] == 0:
            can.append((xx, yy))
    for x, y in can:
        if key_store[x][y] != 0:
            x, y = key_store[x][y]
        if (x, y) not in used:
            cnt += memo[(x, y)]
            used.add((x, y))
    return cnt%10


def dp(a, b):
    # 1. 야 너 arr[x][y], 너에서 출발해서 몇칸 갈 수 있어?
    # 2. 갈 수 있는 칸들 전부 다 memo[(x,y)]에 add해.
    if key_store[a][b] != 0:
        return
    q = deque([(a, b)])
    visited[a][b] = True
    memo[(a, b)] = 0
    while q:
        x, y = q.popleft()
        memo[(a, b)] += 1
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] == 0 and not visited[xx][yy]:
                key_store[xx][yy] = (a, b)
                visited[xx][yy] = True
                q.append((xx, yy))


visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            dp(i, j)

for i in range(n):
    res = ''
    for j in range(m):
        if arr[i][j] == 1:
            res += str(bfs(i, j))
        else:
            res += '0'
    print(res)
