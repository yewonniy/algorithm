import sys
sys.setrecursionlimit(10 ** 6)


def solution(n, info):
    max_diff = 0
    answer = [-1]

    def dfs(L, arrow, ryans, apeachs):
        nonlocal max_diff, answer
        if arrow == 0 or L == 11:  # 끝
            ryan, apeach = 0, 0
            arr = ryans[:]
            if arrow > 0:
                arr[10] += arrow
            for i in range(11):
                if arr[i] == 0 and apeachs[i] == 0:
                    continue  # 아무도 점수 없음
                if arr[i] > apeachs[i]:
                    ryan += (10 - i)
                else:
                    apeach += (10 - i)
            if max_diff < ryan - apeach:
                max_diff = ryan - apeach
                answer = arr
            elif max_diff == ryan - apeach and not (max_diff == ryan-apeach == 0):
                for i in range(10, -1, -1):
                    if arr[i] > answer[i]:
                        answer = arr
                        break
                    elif arr[i] < answer[i]:
                        break
            return
        x = apeachs[L] + 1
        if arrow >= x:
            ryans[L] = x
            dfs(L + 1, arrow - x, ryans, apeachs)  # 쏨
            ryans[L] = 0
        dfs(L + 1, arrow, ryans, apeachs)  # 안쏨

    dfs(0, n, [0] * 11, info)
    return answer

solution(3, [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])