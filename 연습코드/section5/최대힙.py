import heapq
h = []
a = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(h) > 0:
            a.append(-heapq.heappop(h))
        else:
            print(-1)
    else:
        heapq.heappush(h, -n)

res = []
while True:
    x = int(input())
    if x == -1:
        break
    res.append(x)
print(res == a)
