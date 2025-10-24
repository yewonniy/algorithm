def solution(scores): # 근무태도, 동료평가
    for i, arr in enumerate(scores):
        scores[i].append(i)
    dic = {}
    standard = -1
    scores.sort(key=lambda x:(x[0],x[1]))
    for i in range(len(scores)):
        a,b,idx = scores[i]
        for j in range(i+1, len(scores)):
            a2,b2,idx2 = scores[j]
            if a < a2 and b < b2:
                break
        else: # 인센티브 받을 수 잇음
            dic[a+b] = dic.get(a+b, 0) + 1
            if idx == 0:
                standard = a+b
    if standard == -1:
        return -1
    answer = 1
    for x in dic:
        if x > standard:
            answer += dic[x]
    return answer