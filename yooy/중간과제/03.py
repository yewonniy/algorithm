score = list(map(int, input().split()))

memo = []
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            if score[0]*x + score[1]*y + score[2]*z == 100:
                memo.append([x, y, z])

cnt = 0
for x in memo:
    if x[0] != x[1] and x[0] != x[2] and x[1] != x[2]:
        cnt += 1
print(cnt)
