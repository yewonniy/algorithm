v, e = map(int, input().split())
graph = []
for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append([a,b,c])
parents = [i for i in range(v+1)]
graph.sort(key=lambda x:x[2])


def find(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parents[b] = a


res = 0
for a, b, c in graph:
    if find(a) != find(b):
        union(a, b)
        res += c
print(res)