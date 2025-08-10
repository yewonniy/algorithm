from collections import deque
n, k = map(int, input().split())
queue = deque(i for i in range(1,n+1))

while queue:
    if len(queue) == 1:
        break
    for i in range(k):
        x = queue.popleft()
        queue.append(x)
    queue.pop()
print(queue[0])