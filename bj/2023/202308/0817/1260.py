import sys
from collections import deque

n, m, v = map(int, input().split())

line = []
for _ in range(n+1):
    line.append([])

for i in range(m):
    key, value = map(int, sys.stdin.readline().split())
    line[key].append(value)
    line[value].append(key)

for l in line:
    l.sort()

dfs_record = []


def dfs(graph, start, visited):
    visited[start] = 1
    dfs_record.append(start)
    linked = graph[start]
    for i in range(0, len(linked)):
        if visited[linked[i]] == 0:
            dfs(graph, linked[i], visited)
    return dfs_record


dfs_visit = [0] * (n+1)
dfs_result = dfs(line, v, dfs_visit)
for x in dfs_result:
    print(x, end=' ')
print()

bfs_record = []


def bfs(graph, visited, q):
    start = q.popleft()
    visited[start] = 1
    bfs_record.append(start)
    linked = graph[start]
    for i in range(0, len(linked)):
        if visited[linked[i]] == 0:
            q.append(linked[i])
            visited[linked[i]] = 1
    if len(q) > 0: # q에 원소가 있으면
        bfs(graph, visited, q)
        return bfs_record
    else:
        return bfs_record


queue = deque()
queue.append(v)
bfs_visit = [0] * (n+1)
bfs_ans = bfs(line, bfs_visit, queue)
for x in bfs_ans:
    print(x, end=' ')