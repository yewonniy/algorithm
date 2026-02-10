import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())  # m이 가로, n이 세로 0 <= xx < n, 0 <= yy < m
r, c, d = map(int, input().split())  # 0은 위, 1은 오른쪽, 2=아래, 3 = 왼쪽
graph = [list(map(int, input().split())) for _ in range(n)]  # 0이면 청소 안된 칸, 1이면 벽. [r][c]에서 시작
dx = [-1, 0, 1, 0] # 위, 오, 아래, 왼 (d가 0,1,2,3)
dy = [0, 1, 0, -1]


def dfs(x, y, d):
    global cnt
    if graph[x][y] == 0:  # 1. 청소한다.
        graph[x][y] = 2
        cnt += 1
    no_block_to_clean = True
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if 0 <= xx < n and 0 <= yy < m and graph[xx][yy] == 0:
            no_block_to_clean = False
    # 2번 상황 (주변에 청소할 곳 없음)
    if no_block_to_clean:
        # 2-1) 후진
        xx, yy = x - dx[d], y - dy[d]
        if 0 <= xx < n and 0 <= yy < m and graph[xx][yy] != 1:
            return dfs(xx, yy, d)   # 후진이므로 방향은 바뀌지 않는다! dd를 넘기는 것이 아닌, d를 넘겨야 함. (중요!)
        # 2-2) 후진 안되면 작동 멈춤
        else:
            return
    # 3번 상황 (청소할 곳 남음)
    else:
        # 반 시계 방향으로 90도 회전
        for _ in range(4):
            # 0 -> 3, 3 -> 2, 2 -> 1, 1 -> 0
            d = (d-1) % 4
            xx, yy = x + dx[d], y + dy[d]
            if 0 <= xx < n and 0 <= yy < m and graph[xx][yy] == 0:
                return dfs(xx, yy, d)


cnt = 0
dfs(r, c, d)
print(cnt)