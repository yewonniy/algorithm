def solution(survey, choices):
    answer = ''
    type = [('R','T'), ('C','F'), ('J','M'), ('A','N')]
    res = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    n = len(survey) # <= 1,000
    for i in range(n):
        a, b = survey[i][0], survey[i][1]
        k = choices[i]
        if 1 <= k <= 3:
            res[a] += (4-k)
        elif 5<= k <= 7:
            res[b] += (k-4)
    for i in range(4):
        a, b = type[i][0], type[i][1]
        if res[a] >= res[b]:
            answer += a
        else:
            answer += b
    return answer