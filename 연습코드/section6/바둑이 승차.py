c, n = map(int, input().split())
arr = [int(input()) for _ in range(n)]
maxi = 0
total = sum(arr)


def DFS(L, weight, tot):
    global maxi
    if (total-tot) + weight < maxi: # 가지치기!
        return
    if weight > c:
        return
    if L == n:
        maxi = max(maxi, weight)
        return
    DFS(L+1, weight+arr[L], tot+arr[L])
    DFS(L+1, weight, tot+arr[L])


DFS(0, 0, 0)
print(maxi)