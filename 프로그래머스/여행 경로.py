def solution(tickets):
    # tickets를 전부 다!! 사용해야함
    # used_ticket 배열이 전부 True가 될때까지!
    # 백트래킹
    answer = []
    tickets.sort(key=lambda x: (x[0], x[1]))

    def dfs(used, now, ans):
        nonlocal answer
        if len(answer) > 0:
            return
        if all(used):
            tmp = ans[:]
            answer = tmp
            return
        for i, ticket in enumerate(tickets):
            if not used[i] and ticket[0] == now:
                ans.append(ticket[1])
                used[i] = True
                dfs(used, ticket[1], ans)
                ans.pop()
                used[i] = False

    dfs([False] * len(tickets), "ICN", ["ICN"])
    return answer

solution([["ICN", "JFK"], ["ICN", "JFK"], ["JFK", "HND"], ["HND", "ICN"], ["JFK", "ATL"]])