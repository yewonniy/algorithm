# 깊이 우선 탐색
# 스택을 이용! -> 리스트로 구현
# 스택 = 재귀 함수

def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문 (더더 깊은 곳으로)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 담은 2차원 리스트 (0과 연결된 것 없음, 1과 연결된 것 2,3,8 ...)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5]
]

visited = [False] * 5

start = 1
dfs(graph, start, visited)