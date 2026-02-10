from bisect import bisect_left
n = int(input()) # 1,000
arr = list(map(int, input().split()))
# 증가하는 부분 수열의 길이 LIS

res = [arr[0]]
for x in arr:
    if res[-1] < x:
        res.append(x)
    else:
        idx = bisect_left(res, x)
        res[idx] = x
print(len(res))
