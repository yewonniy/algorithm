from collections import deque


def solution(jobs): # 요청 시각, 소요 시간, 작업 번호
    answer = 0
    q = deque()
    for i, l in enumerate(jobs): l.append(i)
    jobs.sort(key=lambda x: (x[0], x[1], x[2]))
    idx = 0
    time = 0
    # print(jobs)
    while idx < len(jobs) or q:
        while idx < len(jobs) and jobs[idx][0] <= time:
            q.append(jobs[idx])
            idx += 1
        if q:
            q = deque(sorted(list(q), key=lambda x:(x[1], x[2])))
            # print(q)
            at, duration, num = q.popleft()
            time += duration
            answer += (time - at)
            # print(num,"번 작업:", time-at)
        else:
            time += 1
    return answer // len(jobs)