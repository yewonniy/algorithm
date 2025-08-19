n = int(input())
graph = input()
stack = []


def DFS(v, visited):
    if not visited[v]:
        visited[v] = True
        print(v, end=' ')
        for x in graph[v]:
            DFS(x, visited)


DFS(1, [False] * (n+1))