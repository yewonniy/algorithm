n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    cnt = 0
    for x in range(x1-1, x2):
        for y in range(y1-1, y2):
            cnt += graph[x][y]
    print(cnt)