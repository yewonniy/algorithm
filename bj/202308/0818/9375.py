import sys

t = int(input())

result = []
for i in range(0, t):
    clothes = {}
    n = int(input())
    for _ in range(n):
        value, key = (sys.stdin.readline().rstrip()).split()
        if key in clothes:
            clothes[key].append(value)
        else:
            clothes[key] = [value]
    if len(clothes) > 1:
        num = 1
        for key in clothes:
            num = num * (len(clothes[key])+1)
        num -= 1
    else:
        num = n
    result.append(num)

for x in result:
    print(x)