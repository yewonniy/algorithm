import sys
input = sys.stdin.readline
INF = float("INF")
n = int(input())
m = int(input())

distance = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    distance[a][a] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    distance[a][b] = min(distance[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            distance[a][b] = min(distance[a][b], distance[a][k]+distance[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == INF:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()