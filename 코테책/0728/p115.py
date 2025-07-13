pos = list(input())
pos[0] = int(ord(pos[0]))-int(ord('a'))+1
pos[1] = int(pos[1])

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

cnt=0

for i in range(8):
    a = pos[0]+steps[i][0]
    b = pos[1]+steps[i][1]
    if a > 0 and b > 0:
        cnt += 1

print(cnt)