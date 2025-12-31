n, m = map(int, input().split()) # 최소 m미터 이상의 나무가 필요
arr = list(map(int, input().split())) # n개의 나무
# binary search : k 미터가 최대가 될 수 있을까?


def binary_search(start, end, res):
    if start > end:
        return res
    mid = (start+end)//2
    cnt = 0
    for x in arr:
        if x > mid:
            cnt += x-mid
    if cnt >= m:
        return binary_search(mid+1, end, max(res, mid))
    else:
        return binary_search(start, mid-1, res)


print(binary_search(0, max(arr),0))