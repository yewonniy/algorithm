n,m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
visited[0][0] = True
broken = False
res = (n+3)*(m+3)
dx = [1,0,-1,0]
dy = [0,1,0,-1]


def dfs(tot, x, y):
    global res, broken
    if x == n-1 and y == m-1:
        res = min(res, tot)
        return
    if tot > res: # 조기리턴
        return
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy]:
            if arr[xx][yy] == 1 and not broken: # 벽 부수고 이동하기
                visited[xx][yy] = True
                broken = True
                dfs(tot+1, xx, yy)
                visited[xx][yy] = False
                broken = False
            elif arr[xx][yy] == 0: # 그냥 이동 가능
                visited[xx][yy] = True
                dfs(tot+1, xx, yy)
                visited[xx][yy] = False


dfs(1, 0, 0)
if res == (n+3)*(m+3):
    print(-1)
else:
    print(res)