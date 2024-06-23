def solution(blocks):  # blocks는 n개의 블럭의 높이
    # 두 블럭이 인접해있어야 하고, 높이가 같거나, 더 높은 블럭으로만 점프 가능.
    res = 0
    for i in range(len(blocks)):
        # x 를 시작 블럭으로 생각하기
        left = i
        right = i
        while True:
            l, r = False, False
            if left - 1 < 0 and right + 1 >= len(blocks):
                break
            if left - 1 >= 0 and blocks[left] <= blocks[left - 1]:
                left = left - 1
                l = True # 움직였다. 가능성 있다
            if right + 1 < len(blocks) and blocks[right] <= blocks[right+1]:
                right = right + 1
                r = True
            if not l and not r:
                break
        res = max(res, right - left + 1)
    return res


print(solution(list(map(int, input().split()))))