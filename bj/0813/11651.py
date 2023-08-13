import sys
n = int(input())
array = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    array.append((x, y))

array.sort(key=lambda data: (data[1], data[0]))
print(array)
for x, y in array:
    print(x, y)