from collections import deque
n, k = map(int, input().split())
q = deque()
q.append((n,0))
visited = dict()
maxi = k-n

while q:
    pos, cnt = q.popleft()
    if pos == k:
        print(cnt)
        break
    if not visited.get(pos*2) and pos*2-k-cnt <= maxi:
        visited[pos*2] = True
        q.append((pos*2, cnt+1))
    if not visited.get(pos+1):
        visited[pos+1] = True
        q.append((pos+1, cnt+1))
    if not visited.get(pos-1):
        visited[pos-1] = True
        q.append((pos-1, cnt+1))
