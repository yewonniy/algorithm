import sys
import heapq
arr = []

n = int(input())

for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(arr) > 0:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, x)
