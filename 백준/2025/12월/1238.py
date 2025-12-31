import sys, heapq
from collections import defaultdict
n, m, x = map(int, sys.stdin.readline().split())  # x 마을에서 파티
x -= 1
distance = [[float('inf')] * n for _ in range(n)] #arr[i][j] => i에서 j까지 시간
dic = defaultdict(list)

for _ in range(m):
    start, end, t = map(int, sys.stdin.readline().split())
    dic[start-1].append((end-1, t))


def dijkstra(start):
    # start부터 각 노드까지의 최단거리
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[start][now] < dist:
            continue
        for next_node, c in dic[now]:
            cost = dist+c
            if cost < distance[start][next_node]:
                distance[start][next_node] = cost
                heapq.heappush(q, (cost, next_node))


for i in range(n):
    distance[i][i] = 0
    dijkstra(i)
res = [0]*n
for i in range(n):
    res[i] += distance[i][x] + distance[x][i]
print(max(res))