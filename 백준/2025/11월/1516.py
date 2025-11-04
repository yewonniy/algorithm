from collections import deque
n = int(input())
dic = {i:[] for i in range(1,n+1)}
time = [0] * (n+1)
degree = [0] * (n+1)
for i in range(1,n+1):
    arr = list(map(int, input().split()))
    for x in arr[1:len(arr)-1]:
        dic[x].append(i)
    time[i] = arr[0]
    degree[i] = len(arr)-2

q = deque()
for i in range(1, n+1):
    if degree[i] == 0:
        q.append((i, time[i]))

answer = [0] * (n+1)
while q:
    node, t = q.popleft()
    answer[node] = t
    for x in dic[node]:
        degree[x] -= 1
        answer[x] = max(t, answer[x])
        if degree[x] == 0:
            q.append((x, answer[x]+time[x]))

for i in range(1, n+1):
    print(answer[i])
