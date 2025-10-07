n, s = map(int, input().split())
arr = list(map(int, input().split()))
lt = 0
rt = -1
tot = 0
min_length = 100001
while True:
    if rt != -1 and (lt > rt or rt > n-1):
        break
    if tot < s:
        rt += 1
        if rt < n:
            tot += arr[rt]
    else:
        min_length = min(min_length, rt-lt+1)
        tot -= arr[lt]
        lt += 1
if min_length == 100001:
    print(0)
else:
    print(min_length)

