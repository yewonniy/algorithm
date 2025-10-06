import sys

sys.setrecursionlimit(10 ** 5)
ans = [0, 10000001]


def dfs(start, x, graph, visited, cnt, summits):
    global ans

    if cnt > ans[1]:  # 조기 리턴
        return

    if x in summits:
        if ans[1] > cnt:
            ans = [x, cnt]
        return

    for y, cost in graph[x]:
        if not visited[y]:
            visited[y] = True
            dfs(start, y, graph, visited, max(cnt, cost), summits)
            visited[y] = False


def solution(n, paths, gates, summits):  # 출입구, (쉼터, 산봉우리 1 ) -> 휴식
    # 휴식 없이 이동해야 하는 시간 중 가장 긴!!! 시간 : intensity
    # dfs (갔던 길로 똑같이 되돌아 온다 -> 가는 것만 찾으면 됨.)
    global ans
    graph = [[] for _ in range(n + 1)]
    for x, y, cost in paths:
        graph[x].append((y, cost))
        graph[y].append((x, cost))

    for i in range(n + 1):
        graph[i].sort(key=lambda x: x[1])

    for x in gates:
        visited = [False] * (n + 1)
        visited[x] = True
        dfs(x, x, graph, visited, 0, summits)

    return ans