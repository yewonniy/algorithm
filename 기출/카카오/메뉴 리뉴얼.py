from itertools import combinations
def solution(orders, course):
# 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성.
# 2가지 이상의 단품메뉴를 포함해야함!
# -> 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함
# 오름차순으로 정렬후 return
    answer = []
    for num in course:
        # num 개 단품 메뉴의 조합이 2번 이상 반복되어야 함.
        cnt = 0
        dic = {}

        for arr in orders:
            comb = list(combinations(list(arr), num))
            for x in comb:
                c = ''.join(sorted(x))
                dic[c] = dic.get(c, 0) + 1

        if len(dic) > 0 :
            max_v = max(list(dic.values()))
            if max_v >= 2:
                for key in dic:
                    if max_v == dic[key]:
                        answer.append(key)
    answer.sort()
    return answer