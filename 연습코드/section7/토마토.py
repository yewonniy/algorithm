from collections import deque
n, m = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(m))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
queue = deque()
for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            queue.append([i, j])

L = -1
while queue:
    size = len(queue)
    for i in range(size):
        a, b = queue.popleft()
        for j in range(4):
            x = a + dx[j]
            y = b + dy[j]
            if 0 <= x < m and 0 <= y < n and arr[x][y] == 0:
                queue.append([x, y])
                arr[x][y] = 1
    L += 1


def check():
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                print(-1)
                return False
    return True


if check():
    print(L)