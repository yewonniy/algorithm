import sys
sys.setrecursionlimit(2000)
s, e = map(int, input().split())
move = [5, 1, -1]
res = 10000000000


def dfs(L, pos):
    global res
    print(L, pos)
    if pos > e or L >= res or (pos < e and pos + (res-L) < e):
        return
    if pos == e:
        res = min(res, L)
        return
    for i in range(3):
        dfs(L+1, pos+move[i])


if s < e:
    dfs(0, s)
else:
    res = s-e
print(res)