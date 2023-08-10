data = [1,1]
n = int(input())
move = list(input().split())

for m in move:
    if m == 'L':
        if data[1]!=1:
            data[1] -= 1
    elif m == 'R':
        if data[1]!=n:
            data[1] += 1
    elif m == 'U':
        if data[0]!=1:
            data[0] -= 1
    else:
        if data[0]!=n:
            data[0] += 1
print(data[0], data[1])
