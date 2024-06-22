n, e = map(int, input().split())  # 노드 수, 간선 수
arr = []
for i in range(e):
    a, b, c = map(int, input().split())
    arr.append([a-1, b-1, c])
v1, v2 = map(int, input().split())
v1 -= 1
v2 -= 1

dis = [[float("inf")] * n for _ in range(n)]
for i in range(e):
    dis[arr[i][0]][arr[i][1]], dis[arr[i][1]][arr[i][0]] = arr[i][2], arr[i][2]
print(dis)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if k == v1 or k == v2:
                dis[i][j] = dis[i][k] + dis[k][j]
                dis[j][i] = dis[i][k] + dis[k][j]
            else:
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
                dis[j][i] = min(dis[i][j], dis[i][k] + dis[k][j])
    print(dis)