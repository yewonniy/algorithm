import sys
sys.setrecursionlimit(10**7)
T = int(input())


def dfs(node): #res = set()
    visited[node] = True
    next_node = degree[node]

    if not visited[next_node]:
        dfs(next_node)
    else:
        if not finished[next_node]:
            cur = next_node
            while cur != node:
                cnt[cur] = 0
                cur = degree[cur]
            cnt[cur] = 0
    finished[node] = True


for _ in range(T):
    n = int(input())
    degree = list(map(lambda x:x-1, list(map(int, input().split()))))
    visited = [False] * n
    finished = [False] * n
    cnt = [1] * n
    for i in range(n):
        if not visited[i]:
            dfs(i)
    print(sum(cnt))