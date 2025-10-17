from collections import deque


def normalize(arr):
    x, y = min(arr)
    new = []
    for a, b in arr:
        new.append((a - x, b - y))
    new.sort(key=lambda x: (x[0], x[1]))
    return new


def rotate(arr):  # 리스트 회전
    new = [(y, -x) for x, y in arr]
    return new


def solution(game_board, table):
    answer = 0
    n, m = len(game_board), len(game_board[0])
    empties = []
    blocks = []

    def bfs(board, x, y, k):
        q = deque()
        q.append((x, y))
        arr = []
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        board[x][y] = k
        while q:
            x, y = q.popleft()
            arr.append((x, y))
            for i in range(4):
                xx, yy = x + dx[i], y + dy[i]
                if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 1 - k:
                    board[xx][yy] = k
                    q.append((xx, yy))
        return arr

    for i in range(n):
        for j in range(m):
            if game_board[i][j] == 0:
                empties.append(normalize(bfs(game_board, i, j, 1)))
            if table[i][j] == 1:
                blocks.append(normalize(bfs(table, i, j, 0)))

    used = [False] * len(blocks)
    used2 = [False] * len(empties)
    for i, block in enumerate(blocks):
        for j, empty in enumerate(empties):
            if len(block) == len(empty) and not used[i] and not used2[j]:
                for _ in range(4):
                    if block == empty:
                        answer += len(block)
                        used[i], used2[j] = True, True
                        break
                    block = normalize(rotate(block))
    return answer