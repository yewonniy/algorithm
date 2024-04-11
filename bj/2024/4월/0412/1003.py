t = int(input())

memo = [(0, 0)] * 41
memo[0] = (1, 0)
memo[1] = (0, 1)
for i in range(2, 41):
    memo[i] = (memo[i-2][0] + memo[i-1][0], memo[i-2][1] + memo[i-1][1])

for _ in range(t):
    n = int(input())
    print(memo[n][0], memo[n][1])