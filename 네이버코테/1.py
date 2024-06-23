def solution(A):
    maxi = max(A)
    check = [0] * (maxi + 1)  # 0 ~ 가장 큰 수
    for x in A:
        check[x] += 1
    res = 0
    for index in range(maxi + 1):
        if index == check[index]:
            res = max(res, index)
    return res


print(solution(list(map(int, input().split()))))
