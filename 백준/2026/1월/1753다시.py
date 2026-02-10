import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
v, e = map(int, input().split())
start = int(input())
dic = defaultdict(list)
for _ in range(e):
    a, b, cost = map(int, input().split())
    dic[a].append((b, cost))
distance = [float('inf')] * (v+1)


def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue
        for next_node, c in dic[now]:
            next_cost = cost + c
            if distance[next_node] > next_cost:
                distance[next_node] = next_cost
                heapq.heappush(q, (next_cost, next_node))


dijkstra(start)
for i in range(1, v+1):
    print(distance[i])