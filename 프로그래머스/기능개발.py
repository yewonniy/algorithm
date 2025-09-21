from collections import deque


def plus(date, q, speeds):
    for i in range(len(q)):
        w, idx = q.popleft()
        q.append([w + speeds[idx] * date, idx])
    return q


def solution(progresses, speeds):
    answer = []
    q = deque()
    for i, x in enumerate(progresses):
        q.append((x, i))

    while q:
        work, idx = q[0]
        cnt = 0
        if (100 - work) % speeds[idx] == 0:
            date = (100 - work) // speeds[idx]
        else:
            date = (100 - work) // speeds[idx] + 1
        q = plus(date, q, speeds)
        while q:
            if q[0][0] >= 100:
                q.popleft()
                cnt += 1
            else:
                break
        answer.append(cnt)
    return answer