import sys
sys.setrecursionlimit(100000)
k, n = map(int, input().split())

sum_ = 0
arr = []
for i in range(k):
    arr.append(int(sys.stdin.readline().rstrip()))
    sum_ += arr[i]
memo = []


def cut(array, cnt, target, start, end):
    if start > end:
        return memo
    mid = (start+end)//2
    for a in array:
        cnt += a//mid
    if target > cnt:
        return cut(array, 0, target, 1, mid-1)
    else:
        memo.append(mid)
        return cut(array, 0, target, mid+1, end)


res = cut(arr, 0, n, 1, max(arr))
print(max(res))