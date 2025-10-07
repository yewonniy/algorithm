def solution(id_list, report, k):
    n = len(id_list)
    graph = [[0] * n for _ in range(n)]
    idx_dic = {id_list[i]: i for i in range(n)}
    answer = [0] * n
    cnt = [0] * n

    stop = set()
    for rep in report:  # x[0] -> x[1]을 신고
        x = rep.split()
        i, j = idx_dic.get(x[0]), idx_dic.get(x[1])
        if graph[i][j] == 0:
            graph[i][j] = 1
            cnt[j] += 1
            if cnt[j] >= k:
                stop.add(j)

    for i in range(n):
        for j in stop:
            if graph[i][j] == 1:
                answer[i] += 1
    return answer