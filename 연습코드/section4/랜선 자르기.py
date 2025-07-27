k, n = map(int, input().split()) # 가지고 있는 랜선 갯수, 만들어야 하는 랜선 갯수
arr = [int(input()) for _ in range(k)]


def binary_search(array, start, end, target, maximum):
    if end < start:
        return maximum
    mid = (start + end) // 2
    cnt = 0
    for n in array:
        cnt += n // mid
    if cnt < target: # mid 값이 더 작아져야함
        return binary_search(array, start, mid-1, target, maximum)
    else:
        return binary_search(array, mid+1, end, target, max(maximum, mid))


print(binary_search(arr, 0, max(arr), n, 0))