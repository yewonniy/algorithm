arr = []


def three_three():
    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]
    for x in range(1, 8, 3):
        for y in range(1, 8, 3):
            ch = [False] * 10
            for i in range(9):
                ch[arr[x + dx[i]][y + dy[i]]] = True
            if not (all(ch[k] for k in range(1, 10))):
                print(x, y, "가 NO")
                return False
    return True


for i in range(9):
    ch = [False] * 10
    arr.append(list(map(int, input().split())))
    for n in arr[i]:
        ch[n] = True
    if not(all(ch[k] for k in range(1, 10))):
        print(i, "번째 열이 NO")
        break
else:
    for y in range(9):
        ch = [False] * 10
        for x in range(9):
            ch[arr[x][y]] = True
        if not (all(ch[k] for k in range(1, 10))):
            print(x, "번째 행이 NO")
            break
    else:
        if three_three():
            print("YES")