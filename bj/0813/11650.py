import sys
n = int(input())

array = []
for i in range(n):
    array.append(tuple(map(int, sys.stdin.readline().split())))

array.sort(key=lambda data: (data[0], data[1]))

print(array)
for x, y in array:
    print(x, y)