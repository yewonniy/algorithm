import heapq
n, m = map(int, input().split()) # n = 문제 수
in_degree = [0] * (n+1)
dic = {i: set() for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    if b not in dic[a]:
        dic[a].add(b)
        in_degree[b] += 1

q = []
answer = []
for i in range(1, n+1):
    if in_degree[i] == 0:
        heapq.heappush(q, i)
while q:
    node = heapq.heappop(q)
    answer.append(node)
    for x in dic[node]:
        in_degree[x] -= 1
        if in_degree[x] == 0:
            heapq.heappush(q, x)

print(' '.join(list(map(str, answer))))