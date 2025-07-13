# 1이 입력되어 있는 곳이 하나의 단지 (n * n)
import sys
sys.setrecursionlimit(200000)


def dfs(arr, x, y):
    if arr[x][y] == '1':
        arr[x][y] = '0'
        house_cnt = 1
        if x+1 < n and arr[x+1][y] == '1':
            house_cnt += dfs(arr, x+1, y)
        if x-1 >= 0 and arr[x-1][y] == '1':
            house_cnt += dfs(arr, x-1, y)
        if y+1 < n and arr[x][y+1] == '1':
            house_cnt += dfs(arr, x, y+1)
        if y-1 >= 0 and arr[x][y-1] == '1':
            house_cnt += dfs(arr, x, y-1)
        return house_cnt
    else:
        return 0


n = int(input())

town = []
for i in range(n):
    town.append(list(input()))

cnt = 0
result = []
for x in range(n):
    for y in range(n):
        if town[x][y] == '1':
            house = dfs(town, x, y)
            if house > 0:
                result.append(house)

print(len(result))
result.sort()
for num in result:
    print(num)
