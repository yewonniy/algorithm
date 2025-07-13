num = list(map(int, input().split()))
a = min(num) - 1
k = 0

while k == 0:
    cnt = 0
    a += 1
    for x in num:
        if a % x == 0:
            cnt += 1
    if cnt >= 3:
        print(a)
        k = 1