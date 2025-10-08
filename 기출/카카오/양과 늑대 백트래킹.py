max_sheep = 0


def dfs(sheep_cnt, wolf_cnt, graph, info, candidate):
    global max_sheep
    if wolf_cnt >= sheep_cnt:
        return
    max_sheep = max(max_sheep, sheep_cnt)
    for i, next_node in enumerate(candidate):
        next_candidate = candidate[:i] + candidate[i + 1:] + graph[next_node]
        if info[next_node] == 0:  # 양!
            dfs(sheep_cnt + 1, wolf_cnt, graph, info, next_candidate)
        else:
            dfs(sheep_cnt, wolf_cnt + 1, graph, info, next_candidate)


def solution(info, edges):
    global max_sheep
    graph = [[] for _ in range(len(info))]
    for x, y in edges:
        graph[x].append(y)

    dfs(1, 0, 0, graph, info, graph[0])
    return max_sheep