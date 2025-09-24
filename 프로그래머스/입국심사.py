def binary_search(n, times, start, end):
    global answer
    mid = (start + end) // 2
    if start > end:
        return answer

    able = 0
    for i in range(len(times)):
        m = mid // times[i]
        able += m
    if able >= n:  # 더 줄여보자
        answer = min(answer, mid)
        return binary_search(n, times, start, mid - 1)
    else:
        return binary_search(n, times, mid + 1, end)


def solution(n, times):
    global answer
    times.sort()
    answer = float('inf')
    binary_search(n, times, 0, times[-1] * n)
    return answer