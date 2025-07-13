n = int(input())

triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

print(triangle)

# [i][j] -> [i+1][j], [i+1][j+1]
def dfs(arr, x, y, cnt):
    if 
    cnt += dfs(arr, x+1, y, cnt)
    cnt += dfs(arr, x+1, y+1, cnt)
    return arr[x][y]


dfs(triangle, 0, 0, 0)