def solution(sequence):
    # dp = [[2,-2], []] # 짝수 인덱스 : 1, -1 홀수 인덱스 : -1, 1
    n = len(sequence)
    dp = [[0, 0] for _ in range(n)]
    dp[0] = [sequence[0], -sequence[0]]
    answer = max(dp[0])
    for i in range(1, n):
        x = sequence[i]
        if i % 2 == 0:
            dp[i][0] = max(x, dp[i - 1][0] + x)
            dp[i][1] = max(-x, dp[i - 1][1] - x)
        else:
            dp[i][0] = max(-x, dp[i - 1][0] - x)
            dp[i][1] = max(x, dp[i - 1][1] + x)
        answer = max(max(dp[i]), answer)
    return answer
