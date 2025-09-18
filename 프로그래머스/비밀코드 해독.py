from itertools import combinations


def solution(n, q, ans):
    answer = 0
    possible = list(combinations(range(1, n+1), 5))
    for i in range(len(possible)):
        cnt = 0
        for j in range(len(q)):
            if len(set(possible[i]) & set(q[j])) == ans[j]:
                cnt += 1
        if cnt == len(q):
            answer += 1
    return answer