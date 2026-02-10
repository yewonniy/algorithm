import sys, heapq
from collections import defaultdict

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    indegree = [0] * (n+1)
    dic = defaultdict(list)

    for _ in range(k):
        a, b = map(int, input().split())
        dic[a].append(b)
        indegree[b] += 1
    w = int(input()) # 이 w 를 건설하는데 걸리는 최소 시간

    q = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(q, (time[i], i))

    while q:
        t, now = heapq.heappop(q)
        if now == w:
            print(t)
            break
        for x in dic[now]:
            indegree[x] -= 1
            if indegree[x] == 0:
                heapq.heappush(q, (t+time[x], x))