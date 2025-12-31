# 1. x 삽입
# 2. 가장 작은 값 출력하고 제거하기
import sys
import heapq

n = int(input())
arr = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))
    else: heapq.heappush(arr, x)
