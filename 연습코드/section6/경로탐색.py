n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
visited = [False] * (n+1)
cnt = 0


def dfs(num):
    global cnt
    if num == n:
        cnt += 1
        return
    visited[num] = True
    for i in range(n+1):
        if graph[num][i] == 1 and not visited[i]:
            dfs(i)
    visited[num] = False


dfs(1)
print(cnt)