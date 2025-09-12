n = int(input())
arr = list()
for i in range(n):
    a = list(input())
    for j in range(n):
        a[j] = int(a[j])
    arr.append(a)
visited = list([False] * n for _ in range(n))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def check_home():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                return [i, j]
    return [-1,-1]


def dfs(L, x, y):
    global cnt
    visited[x][y] = True
    arr[x][y] = 0
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < n and not  visited[new_x][new_y] and arr[new_x][new_y] == 1:
            dfs(L+1, new_x, new_y)
            cnt += 1


county_cnt = 0
res = []
while True:
    cnt = 0
    x, y = check_home()
    if x == -1 and y == -1: # 모든 집 셋음
        break
    county_cnt += 1
    dfs(0, x, y)
    res.append(cnt+1)
res.sort()
print(county_cnt)
for x in res:
    print(x)