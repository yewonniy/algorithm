import sys
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
n, m = n-1, m-1
mini = 100000001
visited = [[False] * (m+1) for _ in range(n+1)]


def dfs(x, y, cnt, wall):
    global mini
    visited[x][y] = True
    if x > n or y > m:
        return
    if x == n and y == m and wall <= 1:
        mini = min(cnt, mini)
        return
    if x - 1 >= 0 and not visited[x-1][y]:
        if graph[x-1][y] == '0':
            dfs(x-1, y, cnt+1, wall)
            visited[x - 1][y] = False
        if graph[x-1][y] == '1' and wall < 1:
            dfs(x-1, y, cnt+1, wall+1)
            visited[x - 1][y] = False
    if x + 1 <= n and not visited[x+1][y]:
        if graph[x+1][y] == '0':
            dfs(x+1, y, cnt+1, wall)
            visited[x+1][y] = False
        if graph[x+1][y] == '1' and wall < 1:
            dfs(x+1, y, cnt+1, wall+1)
            visited[x + 1][y] = False
    if y - 1 >= 0 and not visited[x][y-1]:
        if graph[x][y-1] == '0':
            dfs(x, y-1, cnt+1, wall)
            visited[x][y-1] = False
        if graph[x][y-1] == '1' and wall < 1:
            dfs(x, y-1, cnt+1, wall+1)
            visited[x][y-1] = False
    if y + 1 <= m and not visited[x][y+1]:
        if graph[x][y+1] == '0':
            dfs(x, y+1, cnt+1, wall)
            visited[x][y+1] = False
        if graph[x][y+1] == '1' and wall < 1:
            dfs(x, y+1, cnt+1, wall+1)
            visited[x][y+1] = False


dfs(0, 0, 1, 0)
if mini == 100000001:
    print(-1)
else:
    print(mini)
