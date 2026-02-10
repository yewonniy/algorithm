n, m, x, y, k = map(int, input().split()) # 0 <= xx < n
arr = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split())) # 길이 = k

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dice = [[0] * 3 for _ in range(4)]  # 윗면 = dice[1][1], 바닥면 = dice[3][1]


def rotate(idx):
    if idx == 1:
        tmp = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = tmp
    elif idx == 2:
        tmp = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = tmp
    elif idx == 3:
        tmp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = tmp
    else:
        tmp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = tmp


# 1. arr[i][j] == 0 이면 arr[i][j] = 주사위 바닥
# 2. arr[i][j] != 0 이면 주사위 바닥 = arr[i][j] & arr[i][j] = 0
# 3. 주사위 상단에 쓰인 값 출력
for i in move:
    xx, yy = x + dx[i], y + dy[i]
    if 0 <= xx < n and 0 <= yy < m:
        rotate(i)
        if arr[xx][yy] == 0:
            arr[xx][yy] = dice[3][1]
        else:
            dice[3][1] = arr[xx][yy]
            arr[xx][yy] = 0
        print(dice[1][1])
        x, y = xx, yy