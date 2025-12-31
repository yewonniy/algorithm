#그리디
import sys
n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1],x[0]))
cnt = 0
idx = 0

while idx < n:
    start, end = arr[idx]
    cnt += 1
    for i in range(idx+1, n):
        next_start, next_end = arr[i]
        if next_start >= end:
            idx = i
            break
    else:
        break

print(cnt)