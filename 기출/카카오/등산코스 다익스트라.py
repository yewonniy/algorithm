import heapq
def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    for x, y, cost in paths:
        graph[x].append((y, cost))
        graph[y].append((x, cost))

    summits.sort()
    is_summit = set(summits)

    INF = float('inf')
    intensity = [INF] * (n + 1)
    q = []
    for gate in gates:
        intensity[gate] = 0
        heapq.heappush(q, (0, gate))  # intensity, 노드 순 (현재 위치)
    while q:
        cur_int, node = heapq.heappop(q)
        if node in is_summit or intensity[node] < cur_int:
            continue
        for nxt, cost in graph[node]:
            if intensity[nxt] > max(cur_int, cost):
                intensity[nxt] = max(cur_int, cost)
                heapq.heappush(q, (intensity[nxt], nxt))

    ans = [0, INF]
    for summit in summits:
        if ans[1] > intensity[summit]:
            ans = [summit, intensity[summit]]
    return ans