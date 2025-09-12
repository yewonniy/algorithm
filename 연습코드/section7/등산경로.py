n = int(input())
arr = []
mini = 1000000000
start = [0, 0]
maxi = -1
fin = [0,0]
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] > maxi:
            maxi = a[j]
            fin = [i, j]
        if a[j] < mini:
            mini = a[j]
            start = [i, j]
    arr.append(a)
visited = list([False] * n for _ in range(n))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0


def dfs(L, x, y):
    global cnt
    if x == fin[0] and y == fin[1]:
        cnt += 1
        return
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y] and arr[new_x][new_y] > arr[x][y]:
            dfs(L+1, new_x, new_y)


dfs(0, start[0], start[1])
print(cnt)