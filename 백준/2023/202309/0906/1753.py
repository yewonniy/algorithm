import sys
import heapq
input = sys.stdin.readline
INF = float("INF")
v, e = map(int, input().split())
start_ = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now_node = heapq.heappop(q)
        for x in graph[now_node]:
            node = x[0]
            d = x[1]
            if distance[node] < d+dist:
                continue
            else:
                heapq.heappush(q, (dist+d, node))
                distance[node] = d+dist


dijkstra(start_)
for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])