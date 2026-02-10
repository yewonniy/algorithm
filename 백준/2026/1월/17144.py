import sys
input = sys.stdin.readline
r, c, t = map(int, input().split())  # [r][c]
arr = []
air = []  # [a, b] -> [a][0]과 [b][0]에 공청기 있음
for i in range(r):
    tmp = list(map(int, input().split()))
    for j in range(c):
        if tmp[j] == -1:
            air.append(i)
    arr.append(tmp)
a, b = air

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for _ in range(t):
    graph = [[0] * c for _ in range(r)]
    # 1. 미세먼지 확산 구현
    # a) 몇개의 방향으로 확산되는 지 = cnt, 확산되는 양 =amount, graph = 먼저 양 변화를 저장한 matrix! 바로 arr에 반영하지 않음.
    for x in range(r):
        for y in range(c):
             if arr[x][y] > 0:  # arr[x][y] 에 먼지 존재
                cnt = 0
                amount = arr[x][y] // 5
                # print(arr[x][y], "에서 확산되는 양:", amount)
                if amount > 0:
                    for i in range(4):
                        xx, yy = x + dx[i], y + dy[i]
                        if 0 <= xx < r and 0 <= yy < c and arr[xx][yy] != -1:
                            # 확산 가능하니까 cnt 올리고, 확산시키기
                            cnt += 1
                            graph[xx][yy] += amount
                graph[x][y] -= (amount * cnt)
    for x in range(r):
        for y in range(c):
            arr[x][y] += graph[x][y]

    # 2. 공기청정기 가동
    # [a][0~c-2], [b][0~c-2] row 오른쪽으로 한칸씩 밀림 = 뒷자리를 +1
    # 0번째 column 아래로 밀기
    for row in range(a-1, 0, -1):
        arr[row][0] = arr[row-1][0]
    # 0번째 row 왼쪽으로 밀기
    for column in range(c-1):
        arr[0][column] = arr[0][column+1]
    # 마지막 column 위로 밀기
    for row in range(0, a): # row = 0 ~ a-1
        arr[row][c-1] = arr[row+1][c-1]
    # a번째 row 오른쪽으로 밀기
    for column in range(c-1, 1, -1):
        arr[a][column] = arr[a][column-1]
    arr[a][1] = 0

    # 0번째 column 위 밀기
    for row in range(b+1, r-1): # row = b+1 ~ r-2
        arr[row][0] = arr[row+1][0]
    # 마지막 row 왼쪽으로 밀기
    for column in range(c-1):
        arr[r-1][column] = arr[r-1][column+1]
    # 마지막 column 아래로 밀기
    for row in range(r-1, b, -1): # row = r-1 ~ b+1까지
        arr[row][c-1] = arr[row-1][c-1]
    # b번째 row 오른쪽으로 밀기
    for column in range(c-1, 1, -1): # column = 2 ~ c-1
        arr[b][column] = arr[b][column-1]
    arr[b][1] = 0

res = 2
for i in range(r):
    for j in range(c):
        res += arr[i][j]
print(res)