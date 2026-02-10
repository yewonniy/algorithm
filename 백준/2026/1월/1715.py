import sys, heapq
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

res = 0
while q:
    if len(q) == 1:
        print(res)
        break
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    res += (a+b)
    heapq.heappush(q, a+b)


