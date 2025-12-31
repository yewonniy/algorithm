from collections import defaultdict
n = int(input())
m = int(input())
network = defaultdict(list)
for _ in range(m):
    a,b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)
visited = [False] * (n+1)
res = 0


def dfs(node):
    global res
    if not visited[node]:
        visited[node] = True
        res += 1
    for x in network[node]:
        if not visited[x]:
            dfs(x)


dfs(1)
print(res-1)