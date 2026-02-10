from collections import deque
start, target = map(int, input().split())
MAX = 200001
visited = [0] * MAX


def bfs():
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        num = q.popleft()
        if num == target:
            return visited[num]-1
        for x in (num-1, num+1, num*2):
            if 0 <= x < MAX and visited[x] == 0:
                visited[x] = visited[num] + 1
                q.append(x)


print(bfs())