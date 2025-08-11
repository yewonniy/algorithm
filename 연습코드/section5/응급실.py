from collections import deque
n, m = map(int, input().split()) # 환자 수, 내가 궁금한 환자 번호
arr = list(map(int, input().split()))
queue = deque()
for index, danger in enumerate(arr):
    queue.append((index, danger))

cnt = 0
while queue:
    now_index = queue[0][0]
    now_danger = queue[0][1]
    for j in range(1, len(queue)):
        if now_danger < queue[j][1]:
            queue.append(queue.popleft())
            break
    else: # 진료 받으러 간다!
        queue.popleft()
        cnt += 1
        if now_index == m:
            break
print(cnt)
