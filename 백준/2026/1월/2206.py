import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
F = float("inf")
visited = [[[F, F] for _ in range(m)] for _ in range(n)]
visited[0][0][1] = 0


def bfs():
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0 <= xx < n and 0 <= yy < m and not (xx == 0 and yy == 0):
                if arr[xx][yy] == 1 and visited[x][y][1] != F and visited[xx][yy][0] > visited[x][y][1]+1:  # 벽을 뚫어야 해! arr[x][y]가 벽을 뚫고 온 경우면 안됨
                    visited[xx][yy][0] = visited[x][y][1] + 1
                    q.append((xx, yy))
                if arr[xx][yy] == 0: # 벽을 안뚫어도 됨. 2가지 경우 가능
                    if visited[x][y][0] != F and visited[xx][yy][0] > visited[x][y][0] + 1 and (visited[x][y][1] != F and visited[xx][yy][1] > visited[x][y][1] + 1): # visited[xx][yy][0] 벽 뚫고온 경우 갱신
                        visited[xx][yy][0] = visited[x][y][0] + 1
                        visited[xx][yy][1] = visited[x][y][1] + 1
                        q.append((xx, yy))
                    elif visited[x][y][1] != F and visited[xx][yy][1] > visited[x][y][1] + 1:
                        visited[xx][yy][1] = visited[x][y][1] + 1
                        q.append((xx, yy))
                    elif visited[x][y][0] != F and visited[xx][yy][0] > visited[x][y][0] + 1:
                        visited[xx][yy][0] = visited[x][y][0] + 1
                        q.append((xx, yy))
    res = min(visited[n - 1][m - 1])
    if res == F:
        return -1
    return res + 1


print(bfs())
for i in range(n):
    print(visited[i])

# 7 4
# 0100
# 1110
# 0000
# 1110
# 0000
# 0111
# 0000