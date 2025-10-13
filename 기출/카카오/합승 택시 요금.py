import heapq


def dijkstra(q, s, dis, graph):
    heapq.heappush(q, (0, s))
    dis[s] = 0
    while q:
        cost, node = heapq.heappop(q)
        if dis[node] < cost:
            continue
        for x, c in graph[node]:
            new_cost = cost + c
            if new_cost <= dis[x]:
                dis[x] = new_cost
                heapq.heappush(q, (new_cost, x))


def solution(n, s, a, b, fares):
    # 다익스트라 (최소힙)
    graph = [[] for _ in range(n + 1)]
    for x, y, cost in fares:
        graph[x].append((y, cost))
        graph[y].append((x, cost))

    distance = [[]]
    for i in range(1, n + 1):
        dis = [10 ** 9] * (n + 1)
        dijkstra([], i, dis, graph)
        distance.append(dis)

    res = distance[s][a] + distance[s][b]
    for i in range(1, n + 1):
        res = min(res, distance[s][i] + distance[i][a] + distance[i][b])
    return res