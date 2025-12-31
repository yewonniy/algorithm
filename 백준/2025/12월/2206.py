# n = 1,000 m = 1,000 -> 100만 크기의 맵!
from collections import deque
n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, list(input()))))
dx = [0,1,0,-1]
dy = [-1,0,1,0]
INF = float('inf')
visited = [[[INF, INF] for _ in range(m)] for _ in range(n)] #[이미 벽 부숨, 아직 안부숨]
visited[0][0][1] = 1


def bfs(a, b):
    q = deque()
    q.append([a, b])
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0<=xx<n and 0<=yy<m:
                if grid[xx][yy] == 0 and (visited[x][y][0] + 1 < visited[xx][yy][0] or visited[x][y][1] + 1 < visited[xx][yy][1]):
                    # 벽 안부셔도 됨
                    visited[xx][yy][0] = min(visited[x][y][0] + 1, visited[xx][yy][0])
                    visited[xx][yy][1] = min(visited[x][y][1] + 1, visited[xx][yy][1])
                    q.append([xx, yy])
                elif grid[xx][yy] == 1 and visited[x][y][1]+1 < visited[xx][yy][0]: # 이미 벽 뚫고갓단뜻
                    # 벽 부셔야됨
                    visited[xx][yy][0] = min(visited[xx][yy][0], visited[x][y][1]+1)
                    q.append([xx, yy])
    return


bfs(0, 0)
res = min(visited[n-1][m-1])
if res == INF: res = -1
print(res)