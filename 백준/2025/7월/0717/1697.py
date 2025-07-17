from collections import deque
n, k = map(int, input().split())
MAX_SIZE = 200000
visited = [False] * (MAX_SIZE+1)


def bfs():
    queue = deque()
    queue.append([n, 0])
    while queue:
        left = queue.popleft()
        res = left[0]
        cnt = left[1]
        if res == k:
            return cnt
        if not visited[res]:
            visited[res] = True
            if res+1 <= MAX_SIZE and not visited[res+1]:
                queue.append([res+1, cnt+1])
            if res-1>0 and not visited[res-1]:
                queue.append([res-1, cnt+1])
            if res*2 <= MAX_SIZE and not visited[res*2]:
                queue.append([res*2, cnt+1])


print(bfs())