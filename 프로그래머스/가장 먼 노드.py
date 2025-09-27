from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    dis = [0] * (n+1)

    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        for x in graph[node]:
            if dis[x] == 0 and x != 1:
                dis[x] = dis[node] + 1
                q.append(x)
    return dis.count(max(dis))