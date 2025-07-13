p = [[-4, 4], [-7, 2], [-3, 1], [-5, -2], [-2, -1], [1, -4], [1, 1], [2, 2]]
x = -6
y = 2

p.append(p[0])
count = 0

for i in range(len(p)-1):
    if p[i][1] == p[i+1][1] :
        count = count
    elif p[i][1] == y and x < p[i][0]:
        if p[i+1][1] > p[i][1]:
            count += 1
    elif p[i+1][1] == y and x < p[i+1][0]:
        if p[i][1] > p[i+1][1] :
            count += 1
    else:
        if cross(p[i], p[i+1], [x, y], [100000000000, y]):
            count += 1

if count % 2  == 0:
    print("외부")
else:
    print("내부")