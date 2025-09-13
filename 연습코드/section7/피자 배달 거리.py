from collections import deque
n, m = map(int, input().split())
queue = deque()
cnt = 0
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] == 2:
            queue.append([i, j, cnt])
            cnt += 1
    arr.append(a)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
print(queue)

L = 0
visited = [[[False] * len(queue)] * n for _ in range(n)]
print(visited)
while queue:
    size = len(queue)
    for _ in range(size):
        x, y, cnt = queue.popleft()
        visited[x][y][cnt] = True
        print(visited)
        if arr[x][y] == 1:
            print(cnt, "일 때, [", x,y, "] 에", L,"계단 거쳐 도달")
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy][cnt]:
                queue.append([xx, yy, cnt])
                visited[xx][yy][cnt] = True
    L += 1
