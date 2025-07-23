from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(deque(map(int, input().split())))

m = int(input())
for _ in range(m):
    row, direction, num = map(int, input().split())
    if direction == 0:
        for _ in range(num):
            graph[row-1].append(graph[row-1].popleft())
    else:
        for _ in range(num):
            graph[row-1].appendleft(graph[row-1].pop())

tot = 0
mid = int(n//2)
for i in range(n):
    k = abs(mid-i)
    tot += sum(list(graph[i])[mid-k: mid+k+1])
print(tot)