# 시작 위치에 말 4개
# 화살표대로 이동, 도착칸에 도착하면 끝
# 10번 이동 가능 (매번 4C1)
import sys
sys.setrecursionlimit(10**8)
arr = list(map(int, input().split())) # 주사위
board = [2 * i for i in range(21)] # [0, 2, 4, 6, 8, 10 .. 40] -> L: 0 ~ 20
# L == 5에서 이동하면 board10을 타야함 (L = L + 15 + 주사위 수)
board10 = [13, 16, 19, 25, 30, 35, 40] # L: 21 ~ 27 (idx = L-21)
# L == 10에서 이동하면 board20을 타야함 (L = L + 17 + 주사위 수)
board20 = [22, 24, 25, 30, 35, 40] # L: 28 ~ 33 (idx = L-28)
# L == 15에서 이동하면 board 30을 타야함 (L = L + 18 + 주사위 수)
board30 = [28, 27, 26, 25, 30, 35, 40] # L: 34 ~ 40 (idx = L-34)
# 시간 복잡도 4^10 = 100만
horse = [0, 0, 0, 0] # 현재 인덱스
available = [True, True, True, True]
answer = 0


def check(new_idx):
    if new_idx in horse:
        return False
    if new_idx in (20, 27, 33, 40): # 40에서 겹치는 경우
        for k in horse:
            if k in (20, 27, 33, 40):
                # 불가능
                return False
    elif new_idx in (25, 31, 38):  # 30에서 겹치는 경우
        for k in horse:
            if k in (25, 31, 38):
                return False
    elif new_idx in (26, 32, 39): # 35에서 겹치는 경우
        for k in horse:
            if k in (26, 32, 39):
                return False
    elif new_idx in (24, 30, 37):  # 25에서 겹치는 경우
        for k in horse:
            if k in (24, 30, 37):
                return False
    return True


def dfs(turn, score):
    # turn = 게임 턴, score = 누적 스코어
    global answer
    if turn > 9:
        # print(score, "게임 턴 끝")
        answer = max(score, answer)
        return

    # turn번째 턴에서의 주사위 숫자가 dice_num일때,
    dice_num = arr[turn]
    for i in range(4):  # i번째 말을 이동시킨다면?
        if available[i]:
            now_idx = horse[i]  # = i번째 말이 현재 서 있는 위치
            new_idx = now_idx + dice_num  # = 이번 턴에 이동하게 될 위치
            if now_idx == 5 or (20 < now_idx <= 27):  # 이면 -> board10을 타야함
                if now_idx == 5:
                    new_idx = 20+dice_num  # 파란 선을 타거라
                if new_idx > 27:  # 도착 지점에 도달
                    available[i] = False  # 이제 요 말 사용 불가
                    horse[i] = -1  # 유효하지 않은 말이라는 표시 (이미 도착했다)
                    dfs(turn+1, score)  # 점수 X
                    available[i] = True
                    horse[i] = now_idx
                elif check(new_idx):
                    # 도착 지점이 아니면서, 다른애들이랑도 안겹침
                    horse[i] = new_idx
                    dfs(turn+1, score+board10[new_idx-21])
                    horse[i] = now_idx # 원상 복구
            # 마찬가지인데 board20을 타는 말
            elif now_idx == 10 or 27 < now_idx <= 33:
                if now_idx == 10:
                    new_idx = 27+dice_num
                if new_idx > 33:
                    available[i] = False
                    horse[i] = -1
                    dfs(turn+1, score)
                    available[i] = True
                    horse[i] = now_idx
                elif check(new_idx):
                    horse[i] = new_idx
                    dfs(turn+1, score+board20[new_idx-28])
                    horse[i] = now_idx
            # 마찬가지인데 board30을 타는 말
            elif now_idx == 15 or 33 < now_idx <= 40:
                if now_idx == 15:
                    new_idx = 33+dice_num
                if new_idx > 40:
                    available[i] = False
                    horse[i] = -1
                    dfs(turn+1, score)
                    available[i] = True
                    horse[i] = now_idx
                elif check(new_idx):
                    horse[i] = new_idx
                    dfs(turn+1, score+board30[new_idx-34])
                    horse[i] = now_idx
            # 기본 board를 타는 말
            elif now_idx <= 20:
                if new_idx > 20: # i번째 주사위 탈출!
                    available[i] = False
                    horse[i] = -1
                    dfs(turn+1, score)
                    horse[i] = now_idx
                    available[i] = True
                elif check(new_idx):
                    horse[i] = new_idx
                    dfs(turn+1, score+board[new_idx])
                    horse[i] = now_idx


dfs(0, 0)
print(answer)