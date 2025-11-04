import sys
sys.setrecursionlimit(10**6)
m, n = map(int, input().split()) # 세로 : m, 가로 : n
arr = [list(map(int, input().split())) for _ in range(m)]
memo = [[-1] * n for _ in range(m)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]


def dfs(x, y): # 목표는 (m-1, n-1) <-여기에 도달할 수 있느냐!
    # 내가 (x, y)에서 (m-1, n-1)에 도달할 수 있는지 알려줄게!
    # 일단 memo 부터 확인해보자!
    global answer
    if memo[x][y] != -1:
        return memo[x][y]

    if x == m-1 and y == n-1:
        memo[x][y] = 1
        return 1

    memo[x][y] = 0
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if 0 <= xx < m and 0 <= yy < n and arr[xx][yy] < arr[x][y]:
            # 이동 가능!
            memo[x][y] += dfs(xx, yy)
    return memo[x][y]


answer = dfs(0,0)
print(answer)