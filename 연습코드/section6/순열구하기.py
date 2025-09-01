from itertools import permutations
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
res = list(permutations(arr, m))
# print(res)
# print(len(res))

# DFS로 직접 코드 짜기
def DFS(L, res):
    global cnt
    if L == m:
        print(res)
        cnt += 1
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            DFS(L+1, res + str(arr[i])+" ")
            visited[i] = False


cnt = 0
visited = [False] * n
DFS(0, "")
print(cnt)