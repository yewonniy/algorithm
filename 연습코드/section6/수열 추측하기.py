from itertools import permutations, combinations
n, f = map(int, input().split())
arr = [i for i in range(1, n+1)]
per = list(permutations(arr, n))
ch = False


def dfs(arr):
    global ch
    if len(arr) == 1:
        if arr[0] == f:
            ch = True
            return
        return
    new = []
    for i in range(len(arr)-1):
        k = arr[i] + arr[i+1]
        if k > f:
            return
        new.append(k)
    dfs(new)


# for x in per:
#     dfs(x)
#     if ch:
#         print(x)
#         break
add = []
for i in range(n):
    up = 1
    down = 1
    for j in range(i):
        up *= n-1-j
        down *= (j+1)
    add.append(up//down)

for x in per:
    res = 0
    for i in range(n):
        res += add[i] * x[i]
    if res == f:
        print(x)
        break