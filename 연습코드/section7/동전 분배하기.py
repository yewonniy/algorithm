n = int(input())
coins = list(int(input()) for _ in range(n))
res = 10000000000


def dfs(L, a, b, c):
    global res
    if L == n:
        if a != b and a != c and b != c:
            res = min(res, max(a, b, c) - min(a,b,c))
        return
    coin = coins[L]
    dfs(L+1, a+coin, b, c)
    dfs(L+1, a, b+coin, c)
    dfs(L+1, a, b, c+coin)


dfs(0, 0, 0, 0)
print(res)