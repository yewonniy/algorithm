def solution(friends, gifts):  # 선물지수(준 수 - 받은 수)가 큰 사람이 받음. 더 적게받은 사람이 받음.
    dic = dict()
    l = len(friends)
    for i in range(l):
        dic[friends[i]] = i

    arr = [[0] * l for _ in range(l)]
    cnt = [0] * l  # 받은 수
    for x in gifts:
        give, receive = x.split()
        arr[dic.get(give)][dic.get(receive)] += 1
        cnt[dic.get(receive)] += 1

    gift_rate = []
    for i in range(l):
        gift_rate.append(sum(arr[i]) - cnt[i])
    next = [0] * l

    for i in range(l):
        for j in range(i + 1, l):
            if arr[i][j] < arr[j][i]:
                next[j] += 1
            elif arr[i][j] > arr[j][i]:
                next[i] += 1
            else:
                if gift_rate[i] < gift_rate[j]:  # 선물 지수 비교
                    next[j] += 1
                elif gift_rate[i] > gift_rate[j]:
                    next[i] += 1

    return max(next)