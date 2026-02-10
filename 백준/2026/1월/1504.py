import sys, heapq
input = sys.stdin.readline

n, e = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, cost = map(int, input().split())
    arr[a].append((b, cost))
    arr[b].append((a, cost))
v1, v2 = map(int, input().split())


def dijkstra(start):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))  # 거리, 노드
    while q:
        now_cost, node = heapq.heappop(q)
        for next_node, next_cost in arr[node]:
            new_cost = now_cost + next_cost
            if new_cost < distance[next_node]:  # 갱신
                distance[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))
    return distance


d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(n)
res = min(d1[v1] + d3[v2], d1[v2] + d3[v1]) + d2[v2]
if res == float('inf'):
    res = -1
print(res)

# 6 8
# 1 2 4
# 1 3 3
# 2 3 2
# 2 4 1
# 3 4 4
# 4 5 5
# 4 6 2
# 5 6 1
# 2 3