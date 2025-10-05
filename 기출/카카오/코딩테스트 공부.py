from collections import deque


def solution(alp, cop, problems):  # [알고력, 코딩력, 보상알고력, 보상코딩력, 시간]
    n = len(problems)  # <= 100
    problems.sort(key=lambda x: (x[0], x[1]))
    max_al, max_co = 0, 0  # alp가 max_al이 될때까지, cop가 max_co가 될때까지 최단시간
    for i in range(n):
        max_al = max(problems[i][0], max_al)
        max_co = max(problems[i][1], max_co)

    q = deque()
    q.append((alp, cop, 0))  # time
    answer = float('inf')
    dp = [[float('inf')] * 151 for _ in range(151)]

    while q:
        print(len(q))
        for _ in range(len(q)):
            alp, cop, time = q.popleft()
            dp[alp][cop] = min(dp[alp][cop], time)
            if time < 300:
                if alp >= max_al and cop >= max_co:
                    answer = min(answer, time)
                else:
                    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                        if alp_req > alp:
                            break
                        if alp_req <= alp and cop_req <= cop:
                            if alp + alp_rwd < 151 and cop + cop_rwd < 151 and dp[alp + alp_rwd][
                                cop + cop_rwd] > time + cost and time + cost < answer:
                                q.append((alp + alp_rwd, cop + cop_rwd, time + cost))
                                dp[alp + alp_rwd][cop + cop_rwd] = time + cost
                    if alp < max_al and dp[alp + 1][cop] > time + 1 and time + 1 < answer:
                        q.append((alp + 1, cop, time + 1))
                        dp[alp + 1][cop] = time + 1
                    if cop < max_co and dp[alp][cop + 1] > time + 1 and time + 1 < answer:
                        q.append((alp, cop + 1, time + 1))
                        dp[alp][cop + 1] = time + 1
    return answer