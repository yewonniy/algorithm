n, m = map(int, input().split())  # 사람 수, 파티수
arr = list(map(int, input().split()))
party = []
partner = [[] for _ in range(n + 1)]
for i in range(m):
    l = list(map(int, input().split()))
    party.append(l[1:])  # party
    for j in party[i]:
        for x in party[i]:
            if x != j:
                partner[j].append(x)
# print("파트너들 길이 (n+1) = ",partner)


def dfs(num):
    visited[num] = True
    for x in graph[num]:
        check[x] = True
    for x in partner[num]:
        if not visited[x]:
            dfs(x)


if arr[0] == 0:
    print(m)
else:
    arr = arr[1:]
    visited = [False] * (n+1)
    check = [False] * m
    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(m):
            if i in party[j]:
                graph[i].append(j)
    # print("graph (길이 n+1) = ", graph)
    for i in range(1, n+1):  # i가 사람 번
        if i in arr:
            dfs(i)
    # print(check)
    print(check.count(False))