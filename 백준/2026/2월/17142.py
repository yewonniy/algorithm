import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
# 0 빈칸 1 벽 2 바이러스
n, m = map(int, input().split())  # n = 4~50
arr = []
virus = []
empty_space = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    for j, num in enumerate(tmp):
        if num == 2:
            virus.append((i, j))
        if num == 0:
            empty_space += 1
    arr.append(tmp)
dx = [0,1,-1,0]
dy = [1,0,0,-1]


def bfs(virus_arr, visited):
    global answer
    q = deque()
    cnt, cost = 0, float('inf')
    for v in virus_arr:
        q.append((v, 0))
        visited[v[0]][v[1]] = True
    while q:
        cor, cost = q.popleft()
        x, y = cor
        if cost >= answer:
            return
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy] and (arr[xx][yy] == 0 or arr[xx][yy] == 2):
                if arr[xx][yy] == 0:
                    cnt += 1
                visited[xx][yy] = True
                q.append(((xx, yy), cost+1))
                if cnt == empty_space:
                    answer = min(answer, cost+1)
                    return


if empty_space == 0:
    print(0)
else:
    candidate = list(combinations(virus, m))
    answer = float('inf')
    for c in candidate:
        bfs(c, [[False] * n for _ in range(n)])
    print(-1 if answer == float('inf') else answer)