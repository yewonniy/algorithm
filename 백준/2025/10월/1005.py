from collections import deque
T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    degree = [[] for _ in range(n)]
    indegree = [[] for _ in range(n)]
    ind = [0] * n
    time = list(map(int, input().split()))

    for i in range(k):
        a, b = map(lambda x:x-1, list(map(int, input().split())))  # a 짓고 b a->b
        degree[a].append(b)
        indegree[b].append(a)
        ind[b] += 1
    w = int(input()) - 1

    must = set()
    t = deque([w])
    # len(indegree)가 0이면 q에 추가
    while t:
        x = t.popleft()
        if x not in must:
            must.add(x)
            for y in indegree[x]:
                t.append(y)

    q = deque([i for i in range(n) if ind[i] == 0])
    dp = time[:]
    while q:
        cur = q.popleft()
        for nxt in degree[cur]:
            if nxt in must:
                dp[nxt] = max(dp[nxt], dp[cur]+time[nxt])
                ind[nxt] -= 1
                if ind[nxt] == 0:
                    q.append(nxt)
    print(dp[w])