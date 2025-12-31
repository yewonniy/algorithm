n, k = map(int, input().split())
from collections import deque
maxi = 100001
# bfs?


def bfs(n):
    visited = [False] * maxi
    q = deque()
    q.append(n)
    cnt = 0
    while q:
        l = len(q)
        for _ in range(l):
            x = q.popleft()
            if x == k:
                return cnt
            if x-1 >= 0 and not visited[x-1]:
                visited[x-1] = True
                q.append(x-1)
            if x+1 < maxi and not visited[x+1]:
                visited[x+1] = True
                q.append(x+1)
            if x*2 < maxi and not visited[x*2]:
                visited[x*2] = True
                q.append(x*2)
        cnt += 1


print(bfs(n))