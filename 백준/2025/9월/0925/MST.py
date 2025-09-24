v, e = map(int, input().split())
graph = []
parent = [i for i in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append([a,b,c])
graph.sort(key=lambda x:x[2])


def find_parent(node, parent):
    while parent[node] != node:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return parent[node]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        parent[b] = a


res = 0
for i in range(e):
    a, b, c = graph[i]
    if find_parent(a) != find_parent(b):
        union(a, b)
        res += c
print(res)