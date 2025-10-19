def solution(money):
    n = len(money) - 1
    dp = [[0, 0] for _ in range(n + 1)]
    # 1번 경우의 수 : 첫 집 털고 마지막 집 안털기
    dp[0] = [money[0], 0]
    for i in range(1, n):
        # dp[i][0] : i번째 집 턴다 max(dp[i-1][1] + money[i])
        # dp[i][1] : i번째 집 안턴다 max(dp[i-1][0], dp[i-1][1])
        dp[i][0] = dp[i - 1][1] + money[i]
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
    a = max(dp[n - 1])

    dy = [[0, 0] for _ in range(n + 1)]
    # 2번 경우의 수 : 첫 집 안털고 마지막 집 털기
    for i in range(1, n):
        dy[i][0] = dy[i - 1][1] + money[i]
        dy[i][1] = max(dy[i - 1][0], dy[i - 1][1])
    b = max(dy[n - 1][1] + money[n], dy[n - 1][0])
    return max(a, b)