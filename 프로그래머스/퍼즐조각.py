from collections import deque


def rotate():  # 리스트 회전
    pass


def solution(game_board, table):
    answer = 0
    n, m = len(game_board), len(game_board[0])
    empties = []
    blocks = []

    def bfs(board, x, y, k, l):
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
        l.append(arr)

    for i in range(n):
        for j in range(m):
            if game_board[i][j] == 0:
                bfs(game_board, i, j, 1, empties)
            if table[i][j] == 1:
                bfs(table, i, j, 0, blocks)

    return answer