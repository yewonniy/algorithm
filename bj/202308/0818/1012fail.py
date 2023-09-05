import sys
from collections import deque


def bfs(arr, visit, q, temp):
    pos = q.popleft()
    if pos not in visit:
        visit.append(pos)
    for i in range(len(move)):
        nx = pos[0] + move[i][0]
        ny = pos[1] + move[i][1]
        if (nx >= 0) and (nx <= m-1) and (ny >= 0) and (ny <= n-1):
            new = [nx, ny]
            if (new not in visit) and (new in arr):
                temp = 20
                q.append(new)
                visit.append(new)
    if len(q) > 0:
        return bfs(arr, visit, q, temp)
    if temp == 0:
        return 0
    else:
        return 1


t = int(input())

move = [[0, -1], [0, 1], [-1, 0], [1, 0]] # 상하좌우
visited = []

result = []
for _ in range(t):
    array = []
    cnt = 1
    n, m, k = map(int, input().split())
    for _ in range(k):
        array.append(list(map(int, sys.stdin.readline().split())))
    for i in range(len(array)):
        queue = deque()
        queue.append(array[i])
        res = bfs(array, visited, queue, 0)
        cnt += res
    result.append(cnt)

for x in result:
    print(x)