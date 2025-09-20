import sys
sys.setrecursionlimit(200000)

v, e = map(int, input().split())
edges = []
for i in range(e):
    a,b, c = map(int, sys.stdin.readline().split())
    edges.append([a, b, c])
edges.sort(key=lambda x:x[2])
parent = [0] * (v+1)
res = 0
for i in range(1, v+1):
    parent[i] = i


def find(node):
    #if parent[node] != node:
    #    parent[node] = find(parent[node])
    # 위는 재귀로 구현
    while parent[node] != node:
        parent[node] = parent[parent[node]]
        node = parent[node]
    # 얘는 반복문으로 구현
    return parent[node]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


for a, b, cost in edges:
    if find(a) != find(b):
        union(a,b)
        res += cost
print(res)