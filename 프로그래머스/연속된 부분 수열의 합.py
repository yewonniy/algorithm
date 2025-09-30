def solution(sequence, k):
    answer = [0, 10000000]
    tot = 0
    lt = 0
    rt = 0
    r = True
    while lt <= rt and rt < len(sequence):
        if r:
            tot += sequence[rt]
        else:
            tot -= sequence[lt]
            lt += 1
        if tot == k and answer[1] - answer[0] > rt - lt:
            answer = [lt, rt]
        if tot <= k:
            rt += 1
            r = True
        else:
            r = False
    return answer