import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
# [0][0] => [m-1][n-1]
dx = [-1,0,1,0] # 상좌, 하우
dy = [0,-1,0,1]
dp = [[-1] * n for _ in range(m)]

# 탑 다운 구조의 dp -> 재귀 호출 반복, dp[x][y]가 있으면 반환.
def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    if x == m-1 and y == n-1:
        return 1
    dp[x][y] = 0
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if 0 <= xx < m and 0 <= yy < n and arr[xx][yy] < arr[x][y]:
            dp[x][y] += dfs(xx, yy)
    return dp[x][y]


dfs(0,0)
print(dp[0][0])
print(dp)