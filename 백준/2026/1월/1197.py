import sys

input = sys.stdin.readline
v, e = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(e)]
arr.sort(key=lambda x:x[2])
parent = [i for i in range(v+1)]


def find_parent(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return parent[a]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        parent[a] = b
    return b


res = 0
for a, b, cost in arr:
    if find_parent(a) != find_parent(b):
        union(a, b)
        res += cost
print(res)