def solution(info, edges):
    answer = 0
    graph = {i: [] for i in range(len(info))}
    idx_map = {'sheep': [], 'wolf': []}
    for i, n in enumerate(info):
        if n == 0:
            idx_map['sheep'].append(i)
        else:
            idx_map['wolf'].append(i)

    parents = [0] * len(info)
    for parent, child in edges:
        parents[child] = parent

    for i in range(len(info)):
        parent = parents[i]  # 직속 부모
        graph[i].append(parent)
        while parent != 0:
            parent = parents[parent]
            graph[i].append(parent)

    sheep = []
    for i in range(len(idx_map['sheep'])):
        node = idx_map['sheep'][i]
        sheep.append((len(graph[node]), node))
    sheep.sort()
    wolves = set(idx_map['wolf'])

    sheep_cnt = 0
    wolf_cnt = 0
    visited = [False] * (len(info))
    for in_degree, node in sheep:  # 진입 차수, 노드 번호
        visited[node] = True
        w = 0
        for parent in graph[node]:
            if info[parent] == 1:  # 늑대를 지나야함
                if not visited[parent]:
                    w += 1
                    visited[parent] = True
        wolf_cnt += w
        if sheep_cnt != 0 and wolf_cnt >= sheep_cnt:
            wolf_cnt -= w
        else:
            sheep_cnt += 1
    return sheep_cnt