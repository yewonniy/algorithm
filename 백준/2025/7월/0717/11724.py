from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
visited = [False] * (n + 1)
visited[0] = True


def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


cnt = 0
while False in visited:
    bfs(graph, visited.index(False), visited)
    cnt += 1
print(cnt)
