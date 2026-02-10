import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input().rstrip()))))


def bfs():
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            return arr[x][y]
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] == 1 and not (xx == 0 and yy == 0):
                arr[xx][yy] = 1+arr[x][y]
                q.append((xx, yy))


print(bfs())