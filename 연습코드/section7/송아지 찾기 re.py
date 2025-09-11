from collections import deque
s, e = map(int, input().split())
move = [5, 1, -1]

queue = deque()
queue.append([s, 0])
ch = {s: 0}

while queue:
    pos, cnt = queue.popleft()
    if pos == e:
        break
    for i in range(3):
        new = pos+move[i]
        if ch.get(new) != 0:
            queue.append([new, cnt+1])
            ch[new] = ch.get(new, 0)

print(cnt)

