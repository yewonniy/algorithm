import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드, 간선의 개수
start = int(input()) # 시작 노드
graph = [[] for _ in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
distance = [INF] * (n+1) # 최단 거리 테이블 초기화

# 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split()) # a에서 b 가는 비용이 c
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 시작 노드에서 start 까지의 비용이 0
    distance[start] = 0
    while q: # q가 비어있지 않다면
        dist, now = heapq.heappop(q) # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기
        if distance[now] < dist: # 현재 노드가 이미 처리된 적 있는 노드면
            continue # 무시한다
        for x in graph[now]:
            cost = dist + x[1]
            if cost < distance[x[0]]: # 최단 거리 갱신
                distance[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("도달 불가능")
    else:
        print(distance[i])