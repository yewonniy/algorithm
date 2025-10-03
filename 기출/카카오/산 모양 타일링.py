
def solution(n, tops): # 총 삼각형의 수는 2n + 1개
    p1 = 1
    p2 = 2
    for i in range(n):
        if tops[i] == 1:
            rec = p1 + p2
            p1 = rec + p1
            p2 = rec + p1
        else:
            temp = p1+p2
            p2 = temp + p2
            p1 = temp
    print(p1 % 10007)
    return p1 % 10007


solution(		10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])