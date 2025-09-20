answer = []


def dfs(path, tickets, used):
    global answer
    if len(path) == len(tickets) + 1:
        answer.extend(path)
        return True
    last = path[-1]
    for i, [src, dst] in enumerate(tickets):
        if last == src and not used[i]:
            used[i] = True
            if dfs(path + [dst], tickets, used):
                return True
            used[i] = False
    return False


def solution(tickets):
    global answer
    tickets.sort()
    dfs(["ICN"], tickets, [False] * (len(tickets)))
    return answer


solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])