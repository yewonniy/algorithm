n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = []
for _ in range(n+1):
    graph.append([])

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(v, graph, visit):
    visit[v] = True
    bfs_result = []
    for i in graph[v]:
        if not visit[i]:
            visit[i] = True
            bfs_result.append(i)
    return bfs_result


start, end = min(a, b), max(a, b)
visited = [False] * (n + 1)
cnt = 0
result = [start]
flag = 0

while flag == 0:
    cnt += 1
    if result:
        for x in result:
            result = bfs(x, graph, visited)
            if end in result:
                flag = 1
                print(cnt)
                break
    else:
        print(-1)
        break