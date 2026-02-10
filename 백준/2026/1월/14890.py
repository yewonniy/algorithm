import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]


def slide(start, spot, target, k, increase):  # spot = 칸 높이가 달라진 그 인덱스
    if increase:
        for i in range(k, L+1):
            if spot-i >= 0 and matrix[start][spot-i] == target and not slides[spot-i]:
                slides[spot-i] = True
            else:
                return False
    else:
        for i in range(k, L):
            if spot+i < n and matrix[start][spot+i] == target-1 and not slides[spot+i]:
                slides[spot+i] = True
            else: return False
    return True

def same_height(start, target):
    for y in range(n):
        if matrix[start][y] == target:  # 쭉쭉 검사
            continue
        elif matrix[start][y] == target+1:  # 한 칸 증가
            if not slide(start, y, target,1,  True):
                return False
            target = matrix[start][y]
        elif matrix[start][y] == target-1:  # 한 칸 감소
            if not slide(start, y, target, 0,  False):
                return False
            target = matrix[start][y]
        else:  # 두 칸 이상 점프
            return False
    return True


cnt = 0
for i in range(2):
    for x in range(n):
        slides = [False] * n
        if same_height(x, matrix[x][0]):
            cnt += 1
    # transpose -> 세로가 가로가 됨.
    matrix = (list(map(list, zip(*matrix))))
print(cnt)
