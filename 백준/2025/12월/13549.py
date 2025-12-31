from collections import deque
n, k = map(int, input().split())
visited = [float('inf')] * 100001
visited[n] = 0


q = deque()
q.append([n, 0])
while q:
    pos, time = q.popleft() # 현재 위치, 거기까지 가는데 걸린 시간
    if pos == k:
        break
    if pos-1 >= 0 and visited[pos-1] > time+1:
        visited[pos-1] = time+1 # 1초 써서 -1위치로 이동
        q.append((pos-1, time+1))
    if pos+1 < 100001 and visited[pos+1] > time+1:
        visited[pos+1] = time+1
        q.append((pos+1, time+1))
    if pos*2 < 100001 and visited[pos*2] > time:
        visited[pos*2] = time
        q.appendleft((pos*2, time))
print(visited[k])

