from collections import deque
arr = list(list(map(int, input().split())) for _ in range(7))
distance = list([0] * 7 for _ in range(7))
queue = deque()
queue.append([0, 0])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while queue:
    x, y = queue.popleft()
    if x == 6 and y == 6:
        print(distance[6][6])
        break
    arr[x][y] = 1
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < 7 and 0 <= new_y < 7 and arr[new_x][new_y] == 0:
            queue.append([new_x, new_y])
            distance[new_x][new_y] = distance[x][y] + 1
else:
    print(-1)