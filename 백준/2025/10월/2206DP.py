from collections import deque
n, m = map(int, input().split())
graph = [list(map(int,list(input()))) for _ in range(n)]
visited = [[[False, False] for _ in range(m)] for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

q = deque()
q.append([0,0,1,0])
visited[0][0][0] = True
res = -1
while q:
    for _ in range(len(q)):
        x, y, dist, broken = q.popleft()
        if x == n-1 and y == m-1:
            res = dist
            break
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0 <= xx < n and 0 <= yy < m:
                if graph[xx][yy] == 1 and not visited[xx][yy][broken]:
                    visited[xx][yy][broken] = True
                    q.append([xx, yy, dist+1, broken])
                elif graph[xx][yy] == 0 and not visited[xx][yy][broken]: # 그냥 추가
                    visited[xx][yy][broken] = True
                    q.append([xx, yy, dist+1, broken])

print(res)