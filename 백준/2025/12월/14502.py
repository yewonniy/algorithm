# 최대 64 크기의 격자판
from itertools import combinations
from collections import deque
n, m = map(int, input().split())
graph = []
walls = 3
virus = []
empty = []
for i in range(n):
    l = list(map(int, input().split()))
    graph.append(l)
    for j in range(m):
        if l[j] == 1:
            walls += 1
        if l[j] == 2:
            virus.append([i,j])
        if l[j] == 0:
            empty.append([i, j])
res = 0
safe_place = n*m - walls - len(virus)


def bfs(x, y):
    global newly_conta
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    while q:
        a, b = q.popleft()
        if safe_place-len(newly_conta) <= res:
            return
        for i in range(4):
            xx, yy = a+dx[i], b+dy[i]
            if 0<=xx<n and 0<=yy<m:
                if graph[xx][yy] == 0 and not visited[xx][yy]: # => 새롭게 바이러스 감염!
                    newly_conta.append([xx,yy])
                    q.append((xx, yy))
                    visited[xx][yy] = True
                elif graph[xx][yy] == 2 and not visited[xx][yy]:
                    q.append((xx, yy))
                    visited[xx][yy] = True


combination = list(combinations(range(0,len(empty)), 3))
for comb in combination:
    for com in comb:
        graph[empty[com][0]][empty[com][1]] = 1

    visited = [[False] * m for _ in range(n)]
    newly_conta = [] # 0 -> 2로 새로 감염된 구역 저장
    for x, y in virus:
        if not visited[x][y]: # 아직 전염 여부 확인 안한 바이러스 구역 있으면
            bfs(x, y) # bfs로 확인
    res = max(res, safe_place-len(newly_conta))

    # 벽 세웠던 거 다시 빈 공간으로 원상복구
    for com in comb:
        graph[empty[com][0]][empty[com][1]] = 0
print(res)