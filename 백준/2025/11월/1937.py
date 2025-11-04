import sys
sys.setrecursionlimit(10**6)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)] # (x,y)에서 시작했을때 최대 이동 칸 수
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y): # 내가 (x, y)에서 출발하면 최대 이동 칸 수가 얼마인지 알려줄게!
    # 우선 dp[x][y]에 값이 있는지 확인하자! 이전에 탐색했던 경로일 수 있으니까!
    if dp[x][y] != 0:
        return dp[x][y]
    # 아 처음 가는 길이네!
    # 일단 내가 있는 곳 한 칸은 확보했으니까,
    dp[x][y] = 1
    # 이제 최대값을 갱신해보자!
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if 0 <= xx < n and 0 <= yy < n and arr[xx][yy] > arr[x][y]:
            # 나 (x, y) -> 다음 (xx, yy)
            dp[x][y] = max(dp[x][y], 1+dfs(xx, yy))
    # 이제 dp[x][y]엔 최대 이동 가능 칸 수가 들어있어.
    return dp[x][y]


answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))
print(answer)