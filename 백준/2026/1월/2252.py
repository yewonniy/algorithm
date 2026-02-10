import sys
from collections import defaultdict, deque

input = sys.stdin.readline
n, m = map(int, input().split())
dic = defaultdict(list)
in_degree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    in_degree[b] += 1

q = deque()
for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    print(now, end=' ')
    for x in dic[now]:
        in_degree[x] -= 1
        if in_degree[x] == 0:
            q.append(x)