import sys

input = sys.stdin.readline
n, m = map(int, input().split())  # 최대 25만 0 <= xx < n, 0 <= yy < m
arr = [list(map(int, input().split())) for _ in range(n)]
tetrominos = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],  # tetromino[0] -> [[x,y] .. [x,y]]
    [[0, 0], [1, 0], [2, 0], [3, 0]],  # 위에꺼 회전 시킨 거
    [[0, 0], [0, 1], [1, 0], [1, 1]],

    [[0, 0], [1, 0], [2, 0], [2, 1]],  # 3번재 주황 도형
    [[0, 0], [0, 1], [0, 2], [1, 0]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[1, 0], [1, 1], [1, 2], [0, 2]],
    [[0, 1], [1, 1], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],

    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 1], [0, 2], [1, 0], [1, 1]],
    [[0, 1], [1, 0], [1, 1], [2, 0]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],

    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 1], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [1, 0], [2, 0], [1, 1]],
    [[0, 1], [1, 0], [1, 1], [1, 2]]
]

res = 0
for tetromino in tetrominos:  # 19
    mx, my = float('inf'), float('inf')
    MX, MY = 0, 0
    for x, y in tetromino:  # 4
        MX, MY = max(MX, x), max(MY, y)
        mx, my = min(mx, x), min(my, y)
    for i in range(n - MX):
        for j in range(m - MY):
            cnt = 0
            for x, y in tetromino:
                cnt += arr[x + i][y + j]
            res = max(res, cnt)
print(res)
