from collections import deque
t = int(input())


def bfs(cabbage, x, y):
    queue = deque()
    queue.append((x,y))
    for (x, y) in queue:
        queue.popleft()
        print((cabbage, (x,y)))
        cabbage.remove((x, y))
        if y + 1 < m and (x, y+1) in cabbage:
            queue.append((x, y+1))
            cabbage.remove((x, y+1))
        if x+1 < n and (x+1, y) in cabbage:
            queue.append((x+1, y))
            cabbage.remove((x+1, y))
        if y-1 >= 0 and (x, y-1) in cabbage:
            queue.append((x, y-1))
            cabbage.remove((x, y - 1))
        if x-1 >= 0 and (x-1, y) in cabbage:
            queue.append((x-1, y))
            cabbage.remove((x-1, y))
    return 1


for i in range(t):
    m, n, k = map(int, input().split()) # 가로 세로 배추 갯수

    cabbage = []
    for i in range(k):
        cabbage.append(list((map(int, input().split()))))

    count = 0
    for x, y in cabbage:
        count += bfs(cabbage, x, y)


