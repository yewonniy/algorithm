k, n = map(int, input().split()) # 랜선의 개수, 필요한 개수
arr = [int(input()) for _ in range(k)]


def binary(start, end, ans):
    if start > end:
        print(ans)
        return
    mid = (start + end) // 2
    cnt = 0
    for x in arr:
        cnt += x // mid
    if cnt >= n:
        return binary(mid+1, end, mid)
    else:
        return binary(start, mid-1, ans)


binary(1, max(arr), 0)