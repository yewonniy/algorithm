p = list(map(int, input().split(',')))
m, k = map(int, input().split())

from collections import deque
def solution(players, m, k):
    answer = 0
    server = deque()
    for i in range(24):
        for j in range(len(server)):
            a = server.popleft() - 1
            if a != 0:
                server.append(a)
            else:
                j += 1
        player_num = int(players[i])
        n = player_num // m # n대가 필요하다
        for j in range(n - len(server)): # n - 이미 돌아가는 서버 갯수
            server.append(k)
            answer+=1
    print(answer)
    return answer


solution(p, m, k)