def solution(clothes):
    answer = 1
    dic = {}
    for i in range(len(clothes)):
        new = dic.get(clothes[i][1], [])
        new.append(clothes[i][0])
        dic[clothes[i][1]] = new
    for key in dic.keys():
        answer *= (len(dic.get(key)) +1)
    return answer-1