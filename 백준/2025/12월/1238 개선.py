import heapq
from collections import defaultdict
n, m, x = map(int, input().split())
x -= 1
arr = defaultdict(list)
reverse_arr = defaultdict(list)
for _ in range(m):
    a,b, cost = map(int, input().split())
    arr[a-1].append((b-1, cost))
    reverse_arr[b-1].append((a-1, cost))


def dijkstra(distance, l, x):
    q = []
    heapq.heappush(q, (x, 0))
    # x에서 각 점까지 최소거리!
    while q:
        node, cost = heapq.heappop(q)
        for next_node, dist in l[node]:
            if distance[next_node] < cost+dist:
                continue
            else:
                distance[next_node] = cost+dist
                heapq.heappush(q, (next_node, cost+dist))
    return distance


res = dijkstra([float('inf')] * n, arr, x)
res2 = dijkstra([float('inf')] * n, reverse_arr, x)
res[x], res2[x] = 0, 0
answer = 0
for go, come in zip(res, res2):
    answer = max(answer, go+come)
print(answer)