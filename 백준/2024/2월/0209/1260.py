import sys
from collections import deque

n, m, v = map(int, input().split())
visited_d = [False] * (n+1)
visited_b = [False] * (n+1)

graph = []
for i in range(n+1):
    graph.append([])

for _ in range(m):
    key, value = map(int, sys.stdin.readline().split())
    graph[key].append(value)
    graph[value].append(key)

for i in range(n+1):
    graph[i].sort()


def dfs_(graph, visited, vertex):
    visited[vertex] = True
    print(vertex, end=" ")
    for k in graph[vertex]:
        if not visited[k]:
            dfs_(graph, visited, k)


def bfs_(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for j in graph[vertex]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True


dfs_(graph, visited_d, v)
print()
bfs_(graph, visited_b, v)
