import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]  # dp[x][y] = arr[x][y]보다 큰 애가 몇개?
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y):  # (x, y)에서 최대 몇칸 이동 가능하냐 = (x, y)에서 시작하면 최대 며칠 생존?
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = 1  # 1. 난 일단 이 칸에 있는 대나무 먹고 하루 산다. 그니까 1일
    maxi = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > arr[x][y]: # 이동 가능한 칸
            # 야 너! 나보다 대나무 많은 너 (nx, ny)! 너는 며칠 생존 가능하냐? 물어봐 => dfs 호출
            maxi = max(maxi, dfs(nx, ny))  # 최대값 저장
    dp[x][y] = 1 + maxi
    return dp[x][y]


res = 0
for i in range(n):
    for j in range(n):
        dfs(i, j)
        res = max(res, dp[i][j])
print(res)