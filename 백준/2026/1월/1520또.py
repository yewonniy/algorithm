import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
m, n = map(int, input().split()) # 0 <= xx < m, 0 <= yy < n
arr = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def top_down(x, y):
    # 1. 야 내가 갈 수 있는 위치인 (xx, yy)너! 너에서 출발하면 경로 몇개야?
    # 2. 넵 저 k개 입니다
    # 3. 오키 그럼 난 sum(k)개
    if x == m-1 and y == n-1:
        dp[x][y] = 1
        return 1
    if dp[x][y] != -1: # 0이면 -> 방문해봤는데 더 이상 길이 없단 뜻
        return dp[x][y]
    dp[x][y] = 0
    cnt = 0
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if 0 <= xx < m and 0 <= yy < n and arr[xx][yy] < arr[x][y]:
            cnt += top_down(xx, yy)
    dp[x][y] = cnt
    return dp[x][y]


top_down(0, 0)
print(dp[0][0])