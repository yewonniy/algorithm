# 1세대 드래곤 커브
# 2세대 드래곤 커브 : 맨 처음 1개만 반대로
# 3세대 : 맨처음 2개만 반대로
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)] # x, y, dir, g
dx = [0,-1,0,1]
dy = [1,0,-1,0]


def curve(x, y, gen, move):
    now = 1
    length = 1
    while now <= gen:
        # now 번째 커브 만드는 중
        if now == 1:
            move.append((move[0]+1) % 4)
        else:
            tmp = []
            for i, dir in enumerate(move):
                if i < length//2:
                    tmp.append((dir+2) % 4)
                else:
                    tmp.append(dir)
            move += tmp
        length = len(move)
        now += 1
    # move는 완성.
    cor.add((x, y))
    for dir in move:
        x += dx[dir]
        y += dy[dir]
        cor.add((x, y))


cor = set()
for dragon in arr:
    y, x, dir, g = dragon # g = 세대
    curve(x, y, g, [dir])

res = 0
for x in range(100):
    for y in range(100):
        if (x, y) in cor and (x+1, y) in cor and (x, y+1) in cor and (x+1, y+1) in cor:
            res += 1
print(res)