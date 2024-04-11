import sys
sys.setrecursionlimit(10000)


def dfs(arr, x, y, count):
    if arr[x][y] == 1:
        count = 1
        arr[x][y] = 0
        if y+1 < n:
            dfs(arr, x, y+1, count)
        if y-1 >=0 :
            dfs(arr, x, y-1, count)
        if x+1 < m:
            dfs(arr, x+1, y, count)
        if x-1 >= 0:
            dfs(arr, x-1, y, count)
        return count
    else:
        return count


t = int(input())

for i in range(t):
    m, n, k = map(int, input().split()) # 가로 세로 배추 갯수

    cabbage = [ [0] * n for _ in range(m)]
    cab = []
    for i in range(k):
        x, y = map(int, input().split())
        cab.append((x, y))
        cabbage[x][y] = 1

    cnt = 0
    for x, y in cab:
        cnt += dfs(cabbage, x, y, 0)

    print(cnt)