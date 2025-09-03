from itertools import combinations
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
print(list(combinations(arr, m)))
print(len(list(combinations(arr, m))))

visited = [False] * n
disable = [False] * n


def dfs(L, k):
    global cnt
    res[L] = k
    if L == m-1:
        print(res)
        cnt += 1
        return
    for i in range(1, n):
        if k + i <= n:
            dfs(L+1, k+i)


cnt = 0
res = [0]*m
dfs(-1, 0)
print(cnt)