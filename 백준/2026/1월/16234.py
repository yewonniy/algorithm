# 1. 인접한 국가들 L <= 인구 차이 <= R : 하루 open
# 2. 이동 시작 = 연합
# 3. 각 칸 인구수 = sum 연합 총 인구수 // 연합 칸 개수
import sys
sys.setrecursionlimit(10**9)
n, l, r = map(int, input().split())  # n = 50
arr = [list(map(int, input().split())) for _ in range(n)]  # n*n
boundary = [[0] * n for _ in range(n)]  # 1이면 열린거
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def dfs(x, y, tmp):
    global tot
    visited[x][y] = True
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]  # 인접 국가
        if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy] and l <= abs(arr[xx][yy] - arr[x][y]) <= r:
            visited[xx][yy] = True
            tmp.append((xx, yy))
            tot += arr[xx][yy]
            dfs(xx, yy, tmp)
    return tmp


cnt = 0
while True:
    res = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tot = arr[i][j]
            tmp = dfs(i, j, [(i, j)])
            if len(tmp) > 1:
                tmp.append(tot)
                res.append(tmp)
    if len(res) == 0: break  # 국경 열린 곳 없음 -> 중지
    for tmp in res:
        tot = tmp.pop() // len(tmp)
        for x, y in tmp:
            arr[x][y] = tot
    cnt += 1
print(cnt)