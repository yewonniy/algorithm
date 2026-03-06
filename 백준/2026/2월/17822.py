import sys
from collections import deque
input = sys.stdin.readline
n, m, t = map(int, input().split())
arr = [deque(map(int, input().split())) for _ in range(n)]
order = [list(map(int, input().split())) for _ in range(t)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]


def bfs(a, b):
    q = deque([(a, b)])
    target = arr[a][b]
    arr[a][b] = 0
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] == target:
                q.append((xx, yy))
                arr[xx][yy] = 0
        if y == 0 or y == m-1:
            yy = 0 if y == m-1 else m-1
            if 0 <= x < n and 0 <= yy < m and arr[x][yy] == target:
                q.append((x, yy))
                arr[x][yy] = 0
    if cnt > 1:
        return 1
    arr[a][b] = target
    return 0


def cal():
    sum_ = 0
    valid_cor = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                sum_ += arr[i][j]
                valid_cor.append((i, j))
    if len(valid_cor) == 0:
        return False
    avg = float(sum_) / len(valid_cor)
    for x, y in valid_cor:
        if arr[x][y] > avg:
            arr[x][y] -= 1
        elif arr[x][y] < avg:
            arr[x][y] += 1
    return True


# x의 배수 -1번째 arr를 돌린다. d=0이면 시계 방향 (오른쪽으로 k칸씩), d=1이면 왼쪽으로 k칸씩
for x, d, k in order:
    # 1. 원판 돌리기
    i, idx = 1, x-1
    while idx < n:
        if d == 0:
            arr[idx].rotate(k)
        else:
            arr[idx].rotate(-k)
        i += 1
        idx = x * i - 1
    # 2. 인접한 같은 수 지우기 (지울땐 0 으로)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                cnt += bfs(i, j)
    if cnt == 0:  # 인접하면서 수가 같은 게 없다
        # 3. 평균 구하고 덧셈뺄셈하기
        if not cal():
            break

res = 0
for a in arr:
    res += sum(a)
print(res)