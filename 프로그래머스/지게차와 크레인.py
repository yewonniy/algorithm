from collections import deque


def bfs(target, a, b, n, m, visited, storage):
    if storage[a][b] == target:
        storage[a][b] = "1"
        return
    q = deque()
    q.append([a, b])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy]:
                if storage[xx][yy] == "0":
                    visited[xx][yy] = True
                    q.append([xx, yy])
                elif storage[xx][yy] == target:
                    storage[xx][yy] = "1"
                    visited[xx][yy] = True
    return


def solution(storage, requests):
    answer = 0
    n = len(storage)
    m = len(storage[0])
    for i in range(n):
        storage[i] = list(storage[i])

    for x in requests:
        visited = [[False] * m for _ in range(n)]
        if len(x) == 1:  # 접근 가능한 곳만
            for i in range(n):
                for j in range(m):
                    if (storage[i][j] == "0" or storage[i][j] == x) and (
                            i == 0 or i == n - 1 or j == 0 or j == m - 1) and not visited[i][j]:
                        bfs(x, i, j, n, m, visited, storage)
            for i in range(n):
                for j in range(m):
                    if storage[i][j] == "1":
                        storage[i][j] = "0"
        else:  # 전부 다 빼
            for i in range(n):
                for j in range(m):
                    if storage[i][j] == x[0]:
                        storage[i][j] = "0"

    for i in range(n):
        for j in range(m):
            if storage[i][j] != "0":
                answer += 1
    return answer