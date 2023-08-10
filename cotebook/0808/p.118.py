n, m = map(int, input().split())
x, y, direction = map(int, input().split())

map_ = list()

for i in range(n):
    map_.append(list(map(int, input().split())))

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0]*m for _ in range(n)]
visited[x][y] = 1
turn_time = 0
cnt = 0

while True:
    turn_left()
    turn_time += 1
    nx = x+dx[direction]
    ny = y+dy[direction]
    if map_[nx][ny] == 0 and visited[nx][ny] == 0:
        x = nx
        y = ny
        visited[x][y] = 1
        turn_time = 0
        cnt+=1
        continue
    if turn_time == 4:
        nx = x-dx[direction]
        ny = y-dy[direction]
        if map_[nx][ny] == 0:
            x = nx
            y = ny
            turn_time = 0
        else:
            break
