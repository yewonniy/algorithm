from collections import deque
n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))
visited = list([False] * n for _ in range(n))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
queue = deque()
queue.append([n//2, n//2])
visited[n//2][n//2] = True
L = 0
cnt = 0

while True:
    if L == n//2 + 1:
        break
    size = len(queue)
    for j in range(size):
        x, y = queue.popleft()
        cnt += arr[x][y]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0<= new_y < n and not visited[new_x][new_y]:
                queue.append([new_x, new_y])
                visited[new_x][new_y] = True
    L += 1

print(cnt)