from collections import deque


def bfs(graph, start):
    q = deque(graph[start])
    res = {start}
    visited = [False] * (len(graph))
    visited[start] = True
    while q:
        for i in range(len(q)):
            x = q.popleft()
            if not visited[x]:
                visited[x] = True
                res.add(x)
                for k in graph[x]:
                    q.append(k)
    return len(res)


def solution(n, wires):
    answer = 1000
    for i in range(n - 1):
        graph = [[] for _ in range(n + 1)]
        temp = wires[0:i]
        temp.extend(wires[i + 1::])
        for j in range(n - 2):
            graph[temp[j][0]].append(temp[j][1])
            graph[temp[j][1]].append(temp[j][0])
        res = bfs(graph, temp[0][0])
        answer = min(answer, abs(res - (n - res)))
    return answer