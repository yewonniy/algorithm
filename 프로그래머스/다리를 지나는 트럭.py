from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque()
    q.append([truck_weights[0], 1])
    next = 1
    while q:
        answer+=1
        if answer - q[0][1] == bridge_length:
            q.popleft()
        cnt = 0
        for i in range(len(q)):
            cnt += q[i][0]
        if next < len(truck_weights) and cnt + truck_weights[next] <= weight:
            if answer == 1:
                answer += 1
            q.append([truck_weights[next], answer])
            next += 1
    return answer

solution(100, 100, [10,10,10,10,10,10,10,10,10,10]	)