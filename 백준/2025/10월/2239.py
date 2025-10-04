sdocu = list(list(map(int, list(input())))for _ in range(9))
empties = [(i,j) for i in range(9) for j in range(9) if sdocu[i][j] == 0]


def is_valid(i,j, num):
    if any(sdocu[x][j] == num for x in range(9)): return False
    if any(sdocu[i][y] == num for y in range(9)): return False
    x, y = (i//3)*3, (j//3)*3
    for a in range(x, x+3):
        for b in range(y, y+3):
            if sdocu[a][b] == num:
                return False
    return True


def dfs(idx):
    if idx == len(empties):
        for row in sdocu:
            print(''.join(list(map(str, row))))
        exit(0)
    x, y = empties[idx]
    tmp = list(set(range(1,10)) - set(sdocu[x]))
    for n in tmp:
        if is_valid(x, y, n):
            sdocu[x][y] = n
            dfs(idx+1)
            sdocu[x][y] = 0


dfs(0)