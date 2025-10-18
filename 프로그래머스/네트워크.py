def solution(n, computers):
    answer = 0
    dic = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                dic[i].append(j)
    visited = [False] * n

    def dfs(node):
        visited[node] = True
        for x in dic[node]:
            if not visited[x]:
                dfs(x)

    for node in range(n):
        if not visited[node]:
            dfs(node)
            answer += 1
    return answer