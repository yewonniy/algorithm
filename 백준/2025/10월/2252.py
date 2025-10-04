from collections import deque
n, m = map(int, input().split())
visited = [False] * (n+1) # 큐에 넣은적이 있는지
graph = {}
degree = [0] * (n+1) # 진입차수
for i in range(m):
    a, b = map(int, input().split())
    degree[b] += 1
    tmp = graph.get(a, [])
    tmp.append(b)
    graph[a] = tmp

q = deque()
for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)
        visited[i] = True
answer = []
while q:
    a = q.popleft()
    answer.append(a)
    if graph.get(a):
        for n in graph.get(a):
            degree[n] -= 1
            if degree[n] == 0 and not visited[n]:
                q.append(n)
print(' '.join(list(map(str, answer))))