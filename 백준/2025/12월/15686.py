from itertools import combinations
n, m = map(int, input().split())
arr = []
house = []
chicken = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i, j])
        if arr[i][j] == 2:
            chicken.append([i, j])
distance = [[] for _ in range((len(chicken)))]

for x, y in house:
    for index, c in enumerate(chicken):
        distance[index].append(abs(x-c[0]) + abs(y-c[1]))

comb = list(combinations(range(0,len(chicken)), m))
ans = float('inf')
for l in comb:
    tmp = [float('inf')] * len(house)
    for x in l:
        for i in range(len(house)):
            tmp[i] = min(tmp[i], distance[x][i])
    ans = min(ans, sum(tmp))
print(ans)