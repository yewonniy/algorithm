import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이를 100만까지 늘려줘!

n = int(input())
arr = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, cost = map(int, input().split())
    arr[a-1].append((b-1, cost))
    arr[b-1].append((a-1, cost))
# 루트 노드는 0번


def dfs(node, cost):
    global maximum, maximum_leaf
    # print(node, cost)
    for next_node, next_cost in arr[node]:
        if not visited[next_node]:
            visited[next_node] = True
            if cost + next_cost > maximum:
                maximum = cost + next_cost
                maximum_leaf = next_node
            dfs(next_node, cost+next_cost)


maximum_leaf = 0
for _ in range(2):
    maximum = 0
    visited = [False] * n
    visited[maximum_leaf] = True
    dfs(maximum_leaf, 0)
    # 첫번째 dfs의 결과로 나온 maximum_leaf 노드가 트리의 지름 한쪽 끝!!
    # maximum_leaf를 시작점으로 dfs 한 번 더 돌림
    # 두번째 dfs의 결과로 나온 maximum_leaf의 결과가 다른쪽 지름 끝! maximum = 트리 지름이 됨
print(maximum)
