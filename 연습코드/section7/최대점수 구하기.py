n, m = map(int, input().split()) # 개수, 제한 시간
arr = [list(map(int, input().split())) for _ in range(n)] # 점수, 시간
res = 0


def dfs(L, score, time):
    global res
    if time > m:
        return
    res = max(res, score)
    if L >= n or score + sum(arr[i][0] for i in range(L, n)) < res:
        return
    dfs(L+1, score+arr[L][0], time+arr[L][1])
    dfs(L+1, score, time)


dfs(0, 0, 0)
print(res)