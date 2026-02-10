import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for x in range(1, n):
    arr[x][0] = arr[x-1][0] + arr[x][0]
    arr[x][x] = arr[x-1][x-1] + arr[x][x]
    for y in range(1, x):
        arr[x][y] = max(arr[x-1][y], arr[x-1][y-1]) + arr[x][y]

print(max(arr[-1]))