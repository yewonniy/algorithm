from collections import deque
arr = list(list(map(int, input().split())) for _ in range(7))
visited = list([False] * 7 for _ in range(7))
queue = deque()
queue.append([0, 0])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0


def bfs():
    global cnt
    while True:
        size = len(queue)
        if size == 0:
            cnt = 0
            return
        cnt += 1
        for i in range(size):
            x, y = queue.popleft()
            visited[x][y] = True
            if x == 6 and y == 6:
                return
            for j in range(4):
                new_x = x + dx[j]
                new_y = y + dy[j]
                if 0 <= new_x < 7 and 0 <= new_y < 7 and not visited[new_x][new_y] and arr[new_x][new_y] == 0:
                    queue.append([new_x, new_y])

bfs()
print(cnt-1)