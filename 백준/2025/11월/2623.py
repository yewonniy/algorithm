from collections import deque
n, m = map(int, input().split()) # 가수 수, 피디 수
arr = []
child = {i: set() for i in range(1, n+1)}

degree = [0] * (n+1)
for _ in range(m):
    a = list(map(int, input().split()))
    for i in range(1, a[0]):
        if a[i+1] not in child[a[i]]:
            child[a[i]].add(a[i+1])
            degree[a[i+1]] += 1

used = [False] * (n+1)
q = deque()
for i in range(1,n+1):
    if degree[i] == 0:
        q.append(i)
        used[i] = True
answer = []
while q:
    node = q.popleft()
    answer.append(node)
    for x in child[node]:
        degree[x] -= 1
        if degree[x] <= 0 and not used[x]:
            q.append(x)
            used[x] = True
if len(answer) == n:
    for x in answer: print(x)
else:
    print(0)