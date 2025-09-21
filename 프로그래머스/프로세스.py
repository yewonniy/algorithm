from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()
    for i, x in enumerate(priorities):
        q.append([i, x])
    while q:
        idx, x = q.popleft()
        if any(q[i][1] > x for i in range(len(q))):
            q.append([idx, x])
        else:
            answer += 1
            if idx == location:
                break
    return answer