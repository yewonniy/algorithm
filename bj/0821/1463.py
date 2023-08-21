n = int(input())

memo = [3456798765] * (10**6 + 1)

memo[1] = 0
for i in range(1, n+1):
    if i*3 <= 10**6:
        memo[i*3] = min(memo[i*3], memo[i]+1)
    if i*2 < 10**6:
        memo[i*2] = min(memo[i*2], memo[i]+1)
    if i+1 < 10**6:
        memo[i+1] = min(memo[i+1], memo[i]+1)

print(memo[n])