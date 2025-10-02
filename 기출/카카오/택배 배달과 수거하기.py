def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_idx = n - 1
    pickup_idx = n - 1

    while deliver_idx >= 0 or pickup_idx >= 0:
        # 남은 배달이 없는 경우 인덱스 줄이기
        while deliver_idx >= 0 and deliveries[deliver_idx] == 0:
            deliver_idx -= 1
        # 남은 수거가 없는 경우 인덱스 줄이기
        while pickup_idx >= 0 and pickups[pickup_idx] == 0:
            pickup_idx -= 1

        if deliver_idx < 0 and pickup_idx < 0:
            break  # 모두 완료

        furthest = max(deliver_idx, pickup_idx)  # 가장 먼 위치
        answer += 2 * (furthest + 1)  # 왕복 거리 추가

        cap_deliver = cap
        cap_pickup = cap

        # 배달 처리
        i = deliver_idx
        while i >= 0 and cap_deliver > 0:
            if deliveries[i] > 0:
                if deliveries[i] <= cap_deliver:
                    cap_deliver -= deliveries[i]
                    deliveries[i] = 0
                    i -= 1
                else:
                    deliveries[i] -= cap_deliver
                    cap_deliver = 0
            else:
                i -= 1
        deliver_idx = i

        # 수거 처리
        i = pickup_idx
        while i >= 0 and cap_pickup > 0:
            if pickups[i] > 0:
                if pickups[i] <= cap_pickup:
                    cap_pickup -= pickups[i]
                    pickups[i] = 0
                    i -= 1
                else:
                    pickups[i] -= cap_pickup
                    cap_pickup = 0
            else:
                i -= 1
        pickup_idx = i

    return answer
