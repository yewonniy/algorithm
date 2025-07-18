from collections import deque
n, k = map(int, input().split())


def bfs(graph, start, cnt):
    queue = deque()
    queue.append([start, cnt])
    while queue:
        pop = queue.popleft()
        v = pop[0]
        cnt = pop[1]
        if v == k:
            return cnt
        if not visited[v]:
            visited[v] = True
            for i in graph[v]:
                if 0 <= i <= MAX and cnt+1 <= LIMIT:
                    queue.append([i, cnt+1])


if k < n:
    print(n-k)
else:
    LIMIT = k-n
    MAX = 2*k
    visited = [False] * (2*MAX+1) # 인덱스 : 0 ~ 2k
    graph = [[] for n in range(MAX+1)] # 인덱스 : 0 ~ 2k
    for i in range(MAX+1):
        graph[i].append(i + 1)
        graph[i].append(i-1)
        graph[i].append(i*2)
    print(bfs(graph, n, 0))