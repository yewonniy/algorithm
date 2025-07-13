s1 = list(input())
s2 = list(input())
if len(s2) < len(s1):
    s1, s2 = s2, s1

dy = [[0] * len(s2) for _ in range(len(s1))]
res = []

for i in range(len(s1)):
    for j in range(len(s2)):
        if i == 0:
            if s1[i] == s2[j]:
                dy[i][j] = 1
            else:
                dy[i][j] = dy[i][j-1]
        else:
            if s1[i] == s2[j]:
                if j == 0:
                    dy[i][j] = 1
                else:
                    dy[i][j] = max(dy[i][j-1], dy[i-1][j-1] + 1)
            else:
                if j == 0:
                    dy[i][j] = dy[i-1][j]
                else:
                    dy[i][j] = max(dy[i-1][j], dy[i][j-1])

i = -1
num = max(dy[i])
index = dy[i].index(num)
res = ''
while True:
    if i <= -len(dy):
        break
    while dy[i][index] == num:
        i -= 1
        if i < -len(dy):
            i -= 1
            break
        if dy[i][index] != num:
            res += s1[i + 1]
            index = index - 1
            num = dy[i][index]
            break


if i >= -len(dy) and dy[i][index] == 1:
    res += s1[i]
print(max(dy[-1]))
for i in range(1, len(res)+1):
    print(res[-i], end='')