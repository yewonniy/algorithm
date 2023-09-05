INF = float("INF")

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신 -> 자기 자신은 0으로
for a in range(1, n+1):
    graph[a][a] = 0

# 간선 정보 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 진행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == "INF":
            print('도달 불가', end=' ')
        else:
            print(graph[a][b], end=' ')