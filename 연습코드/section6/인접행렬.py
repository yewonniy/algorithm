n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
graph = [[0] * n for _ in range(n)]

for i in range(m):
    graph[arr[i][0]-1][arr[i][1]-1] = arr[i][2]
print(graph)