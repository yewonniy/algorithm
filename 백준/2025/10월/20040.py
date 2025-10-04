n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
parents = [i for i in range(n)]


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


for i in range(m):
    a, b = graph[i]
    if find(a) == find(b):
        print(i+1)
        break
    else:
        union(a, b)
else:
    print(0)