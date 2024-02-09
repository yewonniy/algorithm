import sys
import heapq
input = sys.stdin.readline
INF = float("INF")
n = int(input()) # 도시 개수
m = int(input()) # 간선 개수
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    a, b, c = map(int, input().split()) # a부터 b까지 비용 c
    graph[a].append((b, c))
start_, destination = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while len(q) > 0:
        dist, now_node = heapq.heappop(q)
        if dist > distance[now_node]:
            continue
        for x in graph[now_node]:
            connected_node = x[0]
            cost = x[1]
            if cost + dist < distance[connected_node]:
                heapq.heappush(q, (cost+dist, connected_node))
                distance[connected_node] = cost + dist


dijkstra(start_) # 1
print(distance[destination]) #distance[5]