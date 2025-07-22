n = int(input())
grid = []
diagonal1 = 0
diagonal2 = 0
for i in range(n):
    l = list(map(int, input().split()))
    grid.append(l)
    diagonal1 += l[i]
    diagonal2 += l[-(i+1)]

res = max(diagonal1, diagonal2)
for i in range(n):
    column = 0
    row = sum(grid[i])
    for j in range(n):
        column += grid[j][i]
    res = max(res, row, column)

print(res)