def solution(alp, cop, problems):
    max_alp = max(max(p[0] for p in problems), alp)
    max_cop = max(max(p[1] for p in problems), cop)

    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    dp[alp][cop] = 0

    for a in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            # 1. 알고력 1 올리기
            if a < max_alp:
                dp[a+1][c] = min(dp[a+1][c], dp[a][c] + 1)
            # 2. 코딩력 1 올리기
            if c < max_cop:
                dp[a][c+1] = min(dp[a][c+1], dp[a][c] + 1)
            # 3. 문제 풀기
            for req_a, req_c, gain_a, gain_c, cost in problems:
                if a >= req_a and c >= req_c:
                    na = min(a + gain_a, max_alp)
                    nc = min(c + gain_c, max_cop)
                    dp[na][nc] = min(dp[na][nc], dp[a][c] + cost)

    return dp[max_alp][max_cop]

