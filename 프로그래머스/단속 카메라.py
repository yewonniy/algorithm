def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    now = 0

    while now < len(routes):
        out = routes[now][1]
        while True:
            if now == len(routes)-1 or not(routes[now+1][0] <= out <= routes[now+1][1]):
                break
            now += 1
        now += 1
        answer += 1
    return answer