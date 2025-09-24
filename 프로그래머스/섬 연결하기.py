def find(parents, node):
    while parents[node] != node:
        parents[node] = parents[parents[node]]
        node = parents[node]
    return parents[node]


def union(a, b, parents):
    a = find(parents, a)
    b = find(parents, b)
    if a != b:
        parents[b] = a


def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    parents = [i for i in range(n)]
    answer = 0
    for a, b, c in costs:
        if find(parents, a) != find(parents, b):
            union(a, b, parents)
            answer += c
    return answer
