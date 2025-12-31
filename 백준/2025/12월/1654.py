import sys
k, n = map(int, input().split())
arr = [int(sys.stdin.readline()) for _ in range(k)]


def binary_search(start, end, res):
    if start > end:
        return res
    mid = (start+end) // 2
    cnt = 0
    for l in arr:
        cnt += l // mid
    if cnt >= n:
        return binary_search(mid+1, end, max(res, mid))
    else:
        return binary_search(start, mid-1, res)


print(binary_search(1, max(arr), 0))