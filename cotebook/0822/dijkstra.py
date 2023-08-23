import sys
input_ = sys.stdin.readline()
INF = int(1e9)

# 노드 갯수, 간선 갯수
n, m = map(int, input().split())
# 시작 정점
start = int(input())
# 각 노드에 연결 되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지
visited = [False] * (n + 1)
# 최단 거리 테이블 을 무한 으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력 받기
for _ in range(m):
    # a 노드 에서 b 노드로 가는 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 방문 하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("도달 불가")
    else:
        print(distance[i])