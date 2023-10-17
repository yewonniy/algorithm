num = list(map(int, input().split()))
M = 3 #최대 자릿수


def digit_func(n, d):
    if n >= (10 ** (d-1)):
        return int(str(n)[-d])
    else:
        return 0


for i in range(1, M+1):
    bucket = list()
    for j in range(0, 10):
        bucket.append(list())
    for x in num:
        bucket[digit_func(x, i)].append(x)
    num = list()
    for j in range(0, 10):
        for x in bucket[j]:
            num.append(x)

print(num)