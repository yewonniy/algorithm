from itertools import combinations
n, m = map(int, input().split())
pizza = list()
home = []
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] == 2:
            pizza.append([i, j])
        if a[j] == 1:
            home.append([i, j])
comb = list(combinations([i for i in range(len(pizza))], m))

dis = [[0] * len(pizza) for _ in range(len(home))]
for i in range(len(home)):
    for j in range(len(pizza)):
        dis[i][j] = abs(home[i][0] - pizza[j][0]) + abs(home[i][1] - pizza[j][1])

res = 10000000
for i in range(len(comb)):
    c = comb[i]
    tot = 0
    for j in range(len(home)):
        mini = 10000000
        for k in range(len(c)):
            mini = min(mini, dis[j][c[k]])
        tot += mini
        if tot > res:
            break
    res = min(res, tot)
print(res)