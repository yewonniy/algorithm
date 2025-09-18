import sys
sys.setrecursionlimit(2000000)
answer = 10**15


def binary_search(start, end, diffs, times, limit):
    global answer
    cnt = 0
    level = (start+end) // 2
    if start > end:
        return level
    for i in range(len(diffs)):
        diff = diffs[i]
        time_cur = times[i]
        time_prev = 0
        if i >= 1:
            time_prev = times[i-1]
        if diff <= level:
            cnt += time_cur
        else:
            cnt += (diff-level) * (time_cur + time_prev) + time_cur
        if cnt > limit : # level 을 높여
            return binary_search(level+1, end, diffs, times, limit)
    if cnt > limit : # level 을 높여
            return binary_search(level+1, end, diffs, times, limit)
    else:
        answer = min(answer, level)
        return binary_search(start, level-1, diffs, times, limit)


def solution(diffs, times, limit):
    global answer
    binary_search(1, limit, diffs, times, limit)
    return answer