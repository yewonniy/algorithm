from collections import deque
n = int(input())
m = int(input())

graph = []
for i in range(n+1):
    graph.append([])

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph, start, visit):
    count = 0
    queue = deque([start])
    visit[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visit[i]:
                visit[i] = True
                queue.append(i)
                count += 1
    print(count)


visited = [False] * (n+1)
bfs(graph, 1, visited)
