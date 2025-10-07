import math
def solution(fees, records):
    # 1. parked 딕셔너리: (차량번호 : 입차 시간)
    # 2. 만약 out이면 해당 차량번호를 찾아서 총 주차시간 계산후 cnt 딕셔너리에 저장
    parked = {}
    cnt = {}
    for record in records:
        time, car, behavior = record.split()
        h, m = map(int, time.split(":"))
        t = (h * 60) + m

        if behavior == "IN":  # 입차
            parked[car] = t
        else:  # 출차
            cnt[car] = cnt.get(car, 0) + (t - parked[car])
            parked[car] = -1

    for car in parked:
        if parked[car] != -1:
            cnt[car] = cnt.get(car, 0) + ((23 * 60 + 59) - parked[car])
    answer = []
    cars = sorted(cnt.keys())
    for car in cars:
        if cnt[car] > fees[0]:
            cost = fees[1] + (math.ceil((cnt[car] - fees[0]) / fees[2]) * fees[3])
            answer.append(cost)
        else:
            answer.append(fees[1])
    return answer