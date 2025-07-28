n, m = map(int, input().split()) # 노래 수, 비디오 수
arr = list(map(int, input().split()))


def binary_search(start, end, res):
    mid = (start + end) // 2
    if start > end:
        return res
    sum = 0
    cnt = 1
    for i in range(n):
        sum += arr[i]
        if sum > mid:
            sum = arr[i]
            cnt += 1
    if cnt > m : # mid를 더 늘려
        return binary_search(mid+1, end, res)
    else:
        return binary_search(start, mid-1, mid)


if m == n:
    print(max(arr))
else:
    print(binary_search(1, sum(arr), 0))