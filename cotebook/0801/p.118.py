n, m = map(int, input().split())
x, y, direction = map(int, input().split())
map_list = []

for i in range(n):
    map_list.append(list(map(int, input().split())))

visited = [[0]*m for _ in range(n)]
visited[x][y] = 1
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

turn_time = 0
cnt = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if map_list[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        turn_time = 0
        cnt += 1
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if map_list[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(map_list)
print(visited)
print(cnt+1)