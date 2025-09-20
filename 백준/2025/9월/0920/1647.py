import sys
n, m = map(int, input().split())
edges = []
for i in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    edges.append([a,b,c])
edges.sort(key=lambda x:x[2])
parent = [i for i in range(n+1)]


def find_parent(node):
    # if parent[node] != node:
    #     parent[node] = find_parent(parent[node])
    while parent[node] != node:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return parent[node]


def union(a, b, cost):
    global max_cost
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        max_cost = max(max_cost, cost)
        parent[b] = a


res = 0
max_cost = 0
for i in range(m):
    a,b,cost = edges[i]
    if find_parent(a) != find_parent(b):
        union(a, b, cost)
        res += cost
print(res-max_cost)