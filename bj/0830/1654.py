import sys
sys.setrecursionlimit(100000)
k, n = map(int, input().split())

sum_ = 0
arr = []
for i in range(k):
    arr.append(int(sys.stdin.readline().rstrip()))
    sum_ += arr[i]


def cut(array, cnt, target, x):
    result = x
    for a in array:
        cnt += a//result
    if target > cnt:
        return cut(array, 0, target, x-1)
    else:
        return result


res = cut(arr, 0, n, sum_//n)
print(res)