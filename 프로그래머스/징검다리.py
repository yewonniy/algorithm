answer = 0


def binary_search(start, end, rocks, n):
    global answer
    mid = (start + end) // 2
    remove = 0
    stack = [rocks[0]]
    if start > end:
        return
    for i in range(1, len(rocks)):
        if rocks[i] - stack[-1] < mid:
            if remove == n:  # 불가능, mid 값을 낮춰
                return binary_search(start, mid - 1, rocks, n)
            remove += 1
        else:
            stack.append(rocks[i])

    answer = max(answer, mid)
    return binary_search(mid + 1, end, rocks, n)


def solution(distance, rocks, n):
    global answer
    rocks.sort()
    rocks.insert(0, 0)
    rocks.append(distance)
    binary_search(0, distance, rocks, n)
    return answer
