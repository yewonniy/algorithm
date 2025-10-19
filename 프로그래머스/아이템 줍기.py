from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    m = 102  # 51
    graph = [[0] * m for _ in range(m)]
    visited = [[False] * m for _ in range(m)]
    for rec in rectangle:
        x1, y1, x2, y2 = [2 * v for v in rec]
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                graph[i][j] = 1
    for rec in rectangle:
        x1, y1, x2, y2 = [2 * v for v in rec]
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                graph[i][j] = 0

    def tot(x, y):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        tot = 0
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < m and 0 <= yy < m:
                tot += graph[xx][yy]
        if tot < 4:
            return True
        return False

    def bfs(a, b):
        q = deque()
        q.append((a, b, 0))
        visited[a][b] = True
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        while q:
            x, y, cnt = q.popleft()
            # print(x, y, cnt, q)
            if x == itemX * 2 and y == itemY * 2:
                print(cnt)
                return cnt
            for i in range(4):
                xx, yy = x + dx[i], y + dy[i]
                if 0 <= xx < m and 0 <= yy < m and graph[xx][yy] == 1 and not visited[xx][yy] and tot(xx, yy):
                    visited[xx][yy] = True
                    q.append((xx, yy, cnt + 1))

    ans = bfs(characterX * 2, characterY * 2)
    return ans // 2