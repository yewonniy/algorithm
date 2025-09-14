n, m = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n)) # 점수, 시간
res = 0


def dfs(L, time, score):
    global res
    if time > m:
        return
    if time == m or L == n:
        res = max(res, score)
        return
    dfs(L+1, time+arr[L][1], score+arr[L][0])
    dfs(L+1, time, score)


dfs(0, 0, 0)
print(res)