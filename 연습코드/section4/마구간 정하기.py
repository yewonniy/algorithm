n, c = map(int, input().split()) # 마굿간, 말 수
arr = [int(input()) for _ in range(n)]
arr.sort()


def binary_search(start, end, res):
    if start > end:
        return res
    mid = (start + end) // 2
    compare_to = 0
    cnt = 1
    next = 1
    sub = max(arr)
    smallest = sub
    for i in range(1, n):
        if arr[i] - arr[compare_to] >= mid:
            compare_to = next
            cnt += 1
            smallest = min(sub, smallest)
        sub = arr[i] - arr[compare_to]
        next = i
    smallest = min(sub, smallest)
    cnt += 1
    print(start, end, mid, "말의 갯수", cnt, ", 가장 가까운 거리", smallest, "이전에 넘어온",res)
    if cnt >= c:
        return binary_search(mid + 1, end, max(res,smallest))
    else: # cnt < c
        return binary_search(start, mid - 1, res)


if c ==2 :
    print(arr[-1]-arr[0])
else:
    print(binary_search(arr[0], arr[-1], 0))

