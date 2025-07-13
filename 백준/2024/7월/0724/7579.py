n, m = map(int, input().split())
m_arr = list(map(int, input().split()))
c_arr = list(map(int, input().split()))

dp = [[0] * (sum(c_arr) + 1) for _ in range(n)]
for i in range(n):
    memory = m_arr[i]  # 얜 m이상
    c = c_arr[i]  # 얜 최소가 되어야 함
    for j in range(sum(c_arr) + 1):
        if i == 0 and j >= c:
            dp[i][j] = memory
        elif i > 0:
            if j >= c:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c] + memory)
            else:
                dp[i][j] = dp[i - 1][j]

for i in range(len(dp[-1])):
    if dp[-1][i] >= m:
        print(i)
        break
