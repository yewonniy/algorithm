arr = list(list(map(int, input().split())) for _ in range(7))
visited = list([False] * 7 for _ in range(7))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
visited[0][0] = True


def dfs(L, x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
        return
    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]
        if 0 <= new_x < 7 and 0 <= new_y < 7 and not visited[new_x][new_y] and arr[new_x][new_y] == 0:
            visited[new_x][new_y] = True
            dfs(L+1, new_x, new_y)
            visited[new_x][new_y] = False


dfs(0, 0, 0)
print(cnt)