import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]  # 체스판 정보
cnt = [[0] * n for _ in range(n)]
# 0: 흰색, 1: 빨강, 2: 파랑
horse = []
horse_arr = [[list() for _ in range(n)] for _ in range(n)]
for i in range(k):
    r, c, dir = map(int, input().split())
    horse.append((r-1, c-1, dir))
    horse_arr[r-1][c-1].append([i, dir]) # i번째 말, 방향
    cnt[r-1][c-1] += 1
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]


def play():
    turn = 0
    check = False
    while True:
        if turn > 1000 or check:  # or 4개가 쌓이면
            return turn

        for i in range(k):  # i번째 말 이동
            x, y, dir = horse[i]  # i번째 말의 좌표와 방향
            xx, yy = x+dx[dir], y+dy[dir]

            # 0. 움직이려는 방향이 파란칸 or 체스판을 벗어나면
            if (0 <= xx < n and 0 <= yy < n and arr[xx][yy] == 2) or not (0 <= xx < n and 0 <= yy < n):
                if dir == 1 or dir == 3: dir += 1
                else: dir -= 1
                xx, yy = x+dx[dir], y+dy[dir]  # 반대방향 탐색

            # 1. 움직이려는 방향이 흰색
            if 0 <= xx < n and 0 <= yy < n and arr[xx][yy] == 0:  # 그대로 이동
                idx = -1
                tmp = deque()
                while idx != i:
                    idx, direction = horse_arr[x][y].pop()
                    tmp.append((idx, direction))
                while tmp:
                    idx, d = tmp.pop()
                    if idx == i: d = dir
                    horse_arr[xx][yy].append([idx, d])  # i번째 말 위에있는 애들을 전부 이동시킴
                    cnt[xx][yy] += 1  # 이동한 칸 (xx, yy)에 말 1개 추가됐다고 표시
                    cnt[horse[idx][0]][horse[idx][1]] -= 1  # 원래 있던 칸에 말 1개 나갔다고 표시
                    horse[idx] = (xx, yy, d) # 이동한 모든 애들의 좌표 정보 바꿔주기
                if cnt[xx][yy] >= 4:
                    check = True

            # 2. 움직이려는 방향이 파란색 or 격자판 벗어나면 이동하지 않고 가마니
            elif (0 <= xx < n and 0 <= yy < n and arr[xx][yy] == 2) or not (0 <= xx < n and 0 <= yy < n):
                horse[i] = (x, y, dir)
                for j in range(len(horse_arr[x][y])):
                    if horse_arr[x][y][j][0] == i:
                        horse_arr[x][y][j][1] = dir

            # 3. 빨간칸
            elif 0 <= xx < n and 0 <= yy < n and arr[xx][yy] == 1:
                idx = -1
                tmp = deque()
                while idx != i:
                    idx, direction = horse_arr[x][y].pop()
                    tmp.append((idx, direction))
                while tmp:
                    idx, d = tmp.popleft()
                    if idx == i: d = dir
                    horse_arr[xx][yy].append([idx, d])  # i번째 말 위에있는 애들을 전부 이동시킴
                    cnt[xx][yy] += 1
                    cnt[horse[idx][0]][horse[idx][1]] -= 1
                    horse[idx] = (xx, yy, d)  # 이동한 모든 애들의 좌표 정보 바꿔주기
                if cnt[xx][yy] >= 4:
                    check = True
        turn += 1


ans = play()
if ans > 1000:
    print(-1)
else:
    print(ans)