import sys
sys.setrecursionlimit(10**6)

v = int(input())
arr = [[] for _ in range(v+1)]
for _ in range(v):
    tmp = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(tmp)-1, 2):
        arr[tmp[0]].append((tmp[i], tmp[i+1]))


# dfs 2번
def dfs(node, cost):
    global maximum_cost, maximum_leaf
    for next_node, next_cost in arr[node]:
        if not visited[next_node]:
            visited[next_node] = True
            if cost+next_cost > maximum_cost:
                maximum_cost = cost + next_cost
                maximum_leaf = next_node
            dfs(next_node, cost+next_cost)


# 1에서 시작
maximum_leaf = 1
for _ in range(2):
    maximum_cost = 0
    visited = [False] * (v+1)
    visited[maximum_leaf] = True
    dfs(maximum_leaf, 0)
print(maximum_cost)