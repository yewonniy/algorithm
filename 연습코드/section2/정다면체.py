from itertools import combinations
n, m = map(int, input().split())

res = [0] * (n+m+1)
for x in range(1, n+1):
    for y in range(1, m+1):
        res[x+y] += 1

ans = max(res)
for i in range(n+m+1):
    if res[i] == ans:
        print(i, end=' ')