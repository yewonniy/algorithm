m, n = map(int, input().split())

tomatoes = []
index = []
for i in range(n):
    tomato = list(map(int, input().split()))
    index.append(list(filter(lambda x: tomato[x] == 1, range(len(tomato)))))
    tomatoes.append(tomato)
print(tomatoes, index)


def dfs(arr, x, y):
    if arr[x][y] == 1: # 맨 처음 입력
        cnt = 0
        if x+1 < n and arr[x+1][y] == 0:
            cnt += dfs(arr, x+1, y)
        if x-1 >= 0 and arr[x-1][y] == 0:
            cnt += dfs(arr, x-1, y)
        if y+1 < m and arr[x][y+1] == 0:
            cnt += dfs(arr, x, y+1)
        if y-1 >= 0 and arr[x][y-1] == 0:
            cnt += dfs(arr, x, y-1)
        return cnt
    if arr[x][y] == 0: # 이후 재귀 반복
        arr[x][y] = 1
        return 1


result = []
for x in range(n):
    for y in index[x]:
        result.append(dfs(tomatoes, x, y))
print(result)