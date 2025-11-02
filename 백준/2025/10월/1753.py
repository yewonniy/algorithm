import heapq
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
start = int(input())
graph = [[] for i in range(v+1)]
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))

dis = [float('inf')] * (v+1)


q = []
heapq.heappush(q, (0, start))
dis[start] = 0
while q:
    cost, node = heapq.heappop(q)
    for new_cost, next_node in graph[node]:
        if dis[next_node] >= cost + new_cost:
            dis[next_node] = cost + new_cost
            heapq.heappush(q, (cost + new_cost, next_node))
for i in range(1, v+1):
    x = dis[i]
    if x == float("inf"):
        x = "INF"
    print(x)