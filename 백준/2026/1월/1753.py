import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
dic = defaultdict(list)
for _ in range(e):
    start, end, cost = map(int, input().split())
    dic[start].append((end, cost))
distance = [float('inf')] * (v+1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        c, now = heapq.heappop(q)
        if distance[now] < c:  # 현재 노드가 이미 처리된 적 있는 노드면
            continue  # 무시한다
        for next, dist in dic[now]:
            cost = c + dist
            if distance[next] > cost:
                heapq.heappush(q, (cost, next))
                distance[next] = cost


dijkstra(k)
for i in range(1, v+1):
    if distance[i] == float('inf'):
        print("INF")
    else:
        print(distance[i])