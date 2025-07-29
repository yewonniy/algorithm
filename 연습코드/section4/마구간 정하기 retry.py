n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()


def binary_search(start, end, res):
    if start > end:
        return res # res는 가장 가까운 두 말의 거리 중 최대값
    mid = (start + end) // 2
    horses = [arr[0]]
    for i in range(n):
        if arr[i] >= horses[-1] + mid:
            horses.append(arr[i])
    if len(horses) >= c:
        return binary_search(mid+1, end, max(mid, res))
    else:
        return binary_search(start, mid-1, res)


print(binary_search(arr[0], arr[-1], 0))