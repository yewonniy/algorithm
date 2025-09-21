v, e = map(int, input().split())
parent = [i for i in range(v+1)]
arr = []
for i in range(e):
    a, b, c = map(int, input().split())
    arr.append([a,b,c])
arr.sort(key=lambda x : x[2])


def find_parent(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        parent[b] = a


res = 0
for i in range(e):
    a,b,c = arr[i]
    if find_parent(a) != find_parent(b):
        union(a, b)
        res += c
print(res)