answer = [0, 0]


def permutation(n, res, emoticons, users):
    global answer
    if len(res) == n:  # len(res) = len(emoticons)
        tot = 0
        plus = 0
        for i in range(len(users)):
            temp = 0
            for j in range(len(emoticons)):
                if users[i][0] <= res[j]:  # 구매
                    temp += (float(100 - res[j]) / 100) * emoticons[j]
            if temp >= users[i][1]:  # 임티 플러스 가입
                plus += 1
            else:  # 그냥 이모티콘 구입
                tot += temp
        if answer[0] < plus:
            answer[0] = plus
            answer[1] = tot
        elif answer[0] == plus:
            answer[1] = max(answer[1], tot)
        return
    for i in range(1, 5):
        res.append(10 * i)
        permutation(n, res, emoticons, users)
        res.pop()


def solution(users, emoticons):  # 10,10,10 / 10,10,20 ... 40,40,40
    global answer, arr
    permutation(len(emoticons), [], emoticons, users)
    print(answer)
    return answer