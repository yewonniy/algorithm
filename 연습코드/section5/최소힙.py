import heapq

heap = []
x = 0
a = []
while x != -1:
    x = int(input())
    if x == -1:
        break
    if x == 0:
        if len(heap) > 0:
            a.append(heapq.heappop(heap))
        else:
            print(-1)
    else:
        heapq.heappush(heap, x)
print(a)
