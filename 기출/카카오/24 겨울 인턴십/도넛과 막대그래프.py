def solution(edges):
    give = dict()
    receive = dict()
    for a, b in edges:
        give[a] = give.get(a, 0) + 1
        receive[a] = receive.get(a, 0)
        receive[b] = receive.get(b, 0) + 1
        give[b] = give.get(b, 0)

    new_node = 1
    for x in list(receive.keys()):
        if receive[x] == 0 and give.get(x) >= 2:
            new_node = x
    answer = [new_node, 0, 0, 0]

    for a, b in edges:  # 새로 삽입된 노드의 방해 간선 없애기
        if a == new_node:
            receive[b] -= 1
    tot = give.pop(new_node)  # 그래프의 총 개수
    receive.pop(new_node)

    for x in list(receive.values()):
        if x == 0:  # 막대 그래프 찾기
            answer[2] += 1
        if x == 2:  # 8자 그래프 찾기
            answer[3] += 1
    answer[1] = tot - (answer[2] + answer[3])

    return answer  # 생성한 정점 번호, 도넛 모양 수, 막대 모양 수, 8자 모양 수