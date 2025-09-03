n, k = map(int, input().split()) # sum(nCk)가 m의 배수인 개수
arr = list(map(int, input().split()))
m = int(input())
res = [0] * k


def dfs(L, index):
    global res, cnt
    res[L] = arr[index]
    if L == k-1:
        # print(res)
        if sum(res) % m == 0:
            cnt += 1
        return
    for i in range(1, n):
        if index + i < n:
            dfs(L+1, index+i)


cnt = 0
dfs(-1, -1)
print(cnt)