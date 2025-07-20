n = int(input())
num = list(map(int, input().split()))


def digit_sum(num : str):
    sum = 0
    for x in num:
        sum += int(x)
    return sum


maxi = 0
ans = num[0]
for x in num:
    res = digit_sum(str(x))
    if res > maxi:
        maxi = res
        ans = x
print(ans)