from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)
    while q:
        tot = q.pop()
        if len(q) > 0 and tot + q[0] <= limit:
            tot += q.popleft()
        answer += 1
    return answer