def solution(plans):
    answer = []
    plan = []
    stack = []
    for name, start, playtime in plans:
        h, m = map(int, start.split(":"))
        plan.append([name, h*60+m, int(playtime)])
    plan.sort(key=lambda x:x[1])

    now = plan[0][1]
    i = 0
    while len(answer) < len(plans):
        name, start, playtime = plan[i] # 이제 진행하려고 하는 과제
        while now < start and stack: # 시작 시간까지 시간이 남아있다면
            remain_t = start-now
            n, s, p = stack.pop()
            if p <= remain_t: # 시간 내에 끝낼 수 있으면
                now += p
                answer.append(n)
            else:
                stack.append([n, s, p-remain_t])
                break
        # 지금 과제 시작 시간 도래
        remain_t = plan[i+1][1] - start
        if playtime <= remain_t: # 시간 내에 끝낼 수 있으면
            answer.append(name)
            now = start + playtime
        else:
            stack.append([name, start, playtime-remain_t])
            now = plan[i+1][1]
        i += 1
        if i == len(plan)-1:
            name, start, playtime = plan[i] # 이제 진행하려고 하는 과제
            while now < start and stack: # 시작 시간까지 시간이 남아있다면
                remain_t = start-now
                n, s, p = stack.pop()
                if p <= remain_t: # 시간 내에 끝낼 수 있으면
                    now += p
                    answer.append(n)
                else:
                    stack.append([n, s, p-remain_t])
                    break
            answer.append(name)
            break
    while stack:
        answer.append(stack.pop()[0])
    return answer
solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]])