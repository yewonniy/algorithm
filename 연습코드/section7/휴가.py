n = int(input())
money = []
time = []
for _ in range(n):
    a, b = map(int, input().split())
    time.append(a)
    money.append(b)
res = 0


def dfs(L, m):
    global res
    res = max(res, m)
    # 종료 지점은 n
    if L == n:
        return
    t = time[L]
    if L+t <= n:
        dfs(L+t, m+money[L])
    if L+1 < n:
        dfs(L+1, m)


dfs(0, 0)
print(res)