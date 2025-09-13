import sys
sys.setrecursionlimit(10000)
arr = list(list(map(int, input().split())) for _ in range(10))
start = arr[9].index(2) # arr[9][start] 가 2의 위치
dx = [0, 0, -1]
dy = [1, -1, 0]


def dfs(x, y):
    global res
    arr[x][y] = 0
    if x == 0:
        res = y
    for i in range(3):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<10 and 0<=yy<10 and arr[xx][yy] == 1:
            dfs(xx, yy)
            break


res = 0
dfs(9, start)
print(res)