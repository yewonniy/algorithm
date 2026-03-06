import sys
input = sys.stdin.readline
n = int(input()) # 1 ~ 20 (드래콘 커브의 개수)
arr = [list(map(int, input().split())) for _ in range(n)]
# [시작x, 시작y, 시작방향, 세대]
dx = [0, -1, 0, 1]  # 오, 아래, 왼, 위
dy = [1, 0, -1, 0]
points = set() # 꼭짓점


def rotate_90(q, last_x, last_y):
    new = []
    min_x, min_y = float('inf'), float('inf')
    # 1) 90도 회전
    for x, y in q:
        new.append((y, -x))
        min_x, min_y = min(min_x, y), min(min_y, -x)

    # 2) normalize
    for i, cor in enumerate(new):
        new[i] = (cor[0]-min_x, cor[1]-min_y)

    # 3) 끝 점과 붙이기
    lx, ly = new.pop()
    a, b = abs(lx - last_x), abs(ly - last_y)
    while new:
        x, y = new.pop()
        q.append((x+a, y+b))

    return


def dfs(q, gen, now_gen): # 도형 꼭짓점 다 찾기
    while now_gen <= gen:
        # now_gen 번째 행위 하는 중
        # 끝 점 (q[-1])을 기준으로 90도 회전 (q = 도형)
        last_x, last_y = q[-1]
        rotate_90(q, last_x, last_y)
        now_gen += 1

    for x, y in q:
        points.add((x, y))
    return


for dragon in arr:
    y, x, d, g = dragon
    # 0gen, 선분 하나 건네주기
    tmp = [(x, y), (x+dx[d], y+dy[d])]
    dfs(tmp, g, 1)

cnt = 0
for x in range(100):
    for y in range(100):
        # x,y가 가장 맨 왼쪽 위 점인 정사각형
        if (x, y) in points and (x+1, y) in points and (x, y+1) in points and (x+1, y+1) in points:
            cnt += 1
print(cnt)