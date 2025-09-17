n, m = map(int, input().split())
dis = [[99999] * (n+1) for i in range(n+1)]
for i in range(m):
    a, b, m = map(int, input().split())
    dis[a][b] = m
    if i <= n:
        dis[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dis[i][j] == 99999:
            print("M", end=' ')
        else:
            print(dis[i][j], end=' ')
    print()