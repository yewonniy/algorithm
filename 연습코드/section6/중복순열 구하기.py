n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
cnt = 0


def DFS(L, res):
    global cnt
    if L == m:
        print(res)
        cnt += 1
        return
    for n in arr:
        DFS(L+1, res + str(n) + " ")


DFS(0, "")
print(cnt)