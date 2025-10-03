from itertools import combinations
res = [0] * 1000


def dfs(L, a, b, n, dice, a_tot, b_tot, A, B, k):
    global res
    if L == n // 2:  # 종료
        A[a_tot] = A.get(a_tot, 0) + 1
        B[b_tot] = B.get(b_tot, 0) + 1
        if sum(A.values()) == 6 ** (n // 2):
            for x in A.keys():
                for y in B.keys():
                    if x > y:
                        res[k] += A[x] * B[y]
        return
    for i in range(6):  # 1~6 혹은 뭐 40~45
        dfs(L + 1, a, b, n, dice, a_tot + dice[a[L]][i], b_tot + dice[b[L]][i], A, B, k)


def solution(dice):  # 나온 수들을 모두 합해 점수 (n/2개의 주사위를 한번씩 굴림)
    global res
    n = len(dice)
    arr = list(combinations(range(n), n // 2))

    for i in range(len(arr)):
        a = arr[i]
        b = list(set(range(n)) - set(a))
        dfs(0, a, b, n, dice, 0, 0, dict(), dict(), i)
    idx = res.index(max(res))
    return list(map(lambda x: x+1, arr[idx]))