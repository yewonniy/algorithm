def dfs(start, graph, visited, res):
    visited[start] = True
    res.append(start)
    for x in graph[start]:
        if not visited[x]:
            dfs(x, graph, visited, res)
    return res


def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    lose_count = [0] * (n + 1)
    win_count = [0] * (n + 1)
    for a, b in results:
        graph[a].append(b)

    win = [0] * (n + 1)
    lose = [0] * (n + 1)
    res = []
    for i in range(1, n + 1):
        res.append(dfs(i, graph, [False] * (n + 1), []))
    for temp in res:
        win[temp[0]] = len(temp) - 1
        for i in range(1, len(temp)):
            lose[temp[i]] += 1
    for i in range(1, n + 1):
        if win[i] + lose[i] == n - 1:
            answer += 1
    return answer