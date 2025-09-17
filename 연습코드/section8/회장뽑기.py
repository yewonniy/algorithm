n = int(input())
dis = [[9999] * (n+1) for _ in range(n+1)]
res = {}
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dis[a][b] = 1
    dis[b][a] = 1

for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

for i in range(1, n+1):
    dis[i][i] = 0
    a = max(dis[i][1::])
    if res.get(a):
        res[a][1].append(i)
        res[a][0] += 1
    else:
        res[a] = [1, [i]]

score = min(res.keys())
print(score, res[score][0])
print(res[score][1])