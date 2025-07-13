n, m = map(int, input().split())

miro = []
for i in range(n):
    miro.append(list(map(int, input())))

cnt = 0
visit = [[0]*m for _ in range(n)]

def bfs(miro, x, y, cnt, visit):
    while True:
        if miro[x][y] == 1 and visit[x][y] == 0:
            visit[x][y] = 1
            cnt += 1
            if x+1 < n and miro[x+1][y] == 1 and visit[x+1][y] == 0:
                x += 1
            elif y+1 < m and miro[x][y+1] == 1 and visit[x][y+1] == 0:
                y += 1
            elif y-1 >= 0 and miro[x][y-1] == 1 and visit[x][y-1] == 0:
                y -= 1
            else:
                x -= 1
        if visit[n-1][m-1] == 1:
            break
    print(cnt)
    print(visit)

bfs(miro, 0, 0, 0, visit)