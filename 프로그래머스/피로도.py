from itertools import permutations
def solution(k, dungeons):
    answer = -1
    p = list(permutations(range(len(dungeons)), len(dungeons)))
    for i in range(len(p)):
        cnt = 0
        kk = k
        for j in p[i]:
            mini, consume = dungeons[j]
            if kk >= mini:
                kk -= consume
                cnt += 1
            else:
                break
        answer = max(cnt, answer)
        if answer == len(dungeons):
            return answer
    return answer