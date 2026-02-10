import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())  # 사과 개수
graph = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
l = int(input())  # 방향 변환 횟수
arr = deque()
for _ in range(l):  # x초에 L(왼쪽) 또는 D(오른쪽)으로 90도 방향 회전한다.
    x, c = input().split()
    arr.append([int(x), c])

time = 0
dx = [-1, 0, 1, 0] # 위 0, 오 1, 아래 2, 왼 3
dy = [0, 1, 0, -1]
d = 1 # 일단 오른쪽을 본 채로 시작

q = deque([(0, 0)])
graph[0][0] = -1
rotate_timing, direction = arr.popleft()

while q:
    # 1. 한 칸 이동
    time += 1  # 1초가 지나서, 한 칸 이동한다.
    x, y = q[0]
    xx, yy = x + dx[d], y + dy[d]  # 뱀 대가리의 위치! (뱀 꼬리 위치 = q.pop())
    if 0 <= xx < n and 0 <= yy < n:
        q.appendleft((xx, yy))
        if graph[xx][yy] == 0:  # 사과가 없다 -> 꼬리 칸을 0으로 바꾸기
            tail_x, tail_y = q.pop()
            graph[tail_x][tail_y] = 0
        elif graph[xx][yy] == -1:  # "몸에 부딪혀서 게임 끝"
            print(time)
            break
        graph[xx][yy] = -1
    else:  # "벽에 부딪혀서 게임 끝"
        print(time)
        break  # 게임 끝
    # 방향 전환
    if time == rotate_timing:
        # if c == D (오른쪽 90도 회전) 이면 "방향 = (방향+1) % 4"
        # if c == L (왼쪽 90도 회전) 이면 "방향 = (방향-1) % 4"
        if direction == "D":
            d = (d+1) % 4
        else:
            d = (d-1) % 4
        if arr:
            rotate_timing, direction = arr.popleft()