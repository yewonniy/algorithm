import sys

input = sys.stdin.readline
n = int(input())
m = int(input())

arr = [[float('inf')] * n for _ in range(n)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    arr[start-1][end-1] = min(arr[start-1][end-1], cost)
for i in range(n):
    arr[i][i] = 0

# 최대 100만번 반복 -> 시간은 충분
for k in range(n):
    for i in range(n):
        for j in range(n):
            cost = arr[i][k] + arr[k][j]
            if cost < arr[i][j]:
                arr[i][j] = cost

for i in range(n):
    for x in arr[i]:
        if x == float('inf'):
            x = 0
        print(x, end=' ')
    print()