def deletionNeed(ty, tm, td, y, m, d, valid): # 현재 날짜, 시작 날짜, 유효 기간
    new_m = m + (d + valid) // 28 # 만큼 m를 ++
    new_d = (d + valid) % 28 # 만큼 d를 ++
    new_y = y
    if new_m > 12:
        new_y = y + (new_m // 12)
        new_m = new_m % 12
        if new_m % 12 == 0:
            new_y -= 1
            new_m = 12
    if new_y > ty: # 아직 파기 날짜 도래X
        return False
    if new_y < ty: # 파기 날짜 지남.
        return True
    # 연도는 같음 -> 달 비교
    if new_m > tm:
        return False
    if new_m < tm:
        return True
    # 달도 같음 -> 날짜 비교
    if new_d <= td:
        return True
    return False


def solution(today, terms, privacies):
    term = dict()
    answer = []
    t_y, t_m, t_d = map(int, today.split("."))
    for i in range(len(terms)):
        a, m = terms[i].split(" ")
        term[a] = int(m) * 28
    for i in range(len(privacies)):
        start, name = privacies[i].split(" ")
        year, m, d = map(int, start.split("."))
        if deletionNeed(t_y, t_m, t_d, year, m, d, term[name]):
            answer.append(i+1)
    return answer