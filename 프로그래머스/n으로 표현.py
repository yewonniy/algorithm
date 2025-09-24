def solution(n, number):
    answer = 0
    cnt = [set() for _ in range(9)]
    for i in range(1, 9):
        cnt[i].add(int(str(n)*i))
        for j in range(1, i):
            for op1 in cnt[j]:
                for op2 in cnt[i-j]:
                    cnt[i].add(op1+op2)
                    cnt[i].add(op1-op2)
                    cnt[i].add(op1*op2)
                    if op2 != 0:
                        cnt[i].add(op1//op2)
        if number in cnt[i]:
            return i
    return -1