n, s = map(int, input().split())
arr = list(map(int, input().split()))
lt = 0
rt = 0
res = 10000000
tot = 0
while True:
    if (rt == n and tot < s) or lt == n:
        break
    if tot >= s:
        res = min(res, rt-lt)
        tot -= arr[lt]
        lt += 1
    elif tot < s:
        tot += arr[rt]
        rt += 1

if res == 10000000:
    print(0)
else:
    print(res)