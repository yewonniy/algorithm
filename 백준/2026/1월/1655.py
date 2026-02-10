import sys, heapq
from bisect import bisect_left
from collections import deque

input = sys.stdin.readline
n = int(input())  # 10만

k = int(input()) + 10000
# 어떤 자료구조를 써야 하느냐..........
print(k-10000)
left = []
right = []
# len(right) - len(left) == 1 or 0
for i in range(1, n):
    x = int(input()) + 10000
    if x >= k:
        heapq.heappush(right, x)
    else:
        heapq.heappush(left, -x)
    if len(right) - len(left) > 1:
        heapq.heappush(left, -k)
        k = heapq.heappop(right)
    elif len(left) - len(right) == 1:
        heapq.heappush(right, k)
        k = -heapq.heappop(left)
    print(k-10000)



