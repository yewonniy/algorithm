num = list(map(int, input().split()))

for i in range(1, len(num)):
    now = num[i]
    j = i-1
    while j >= 0:
        if num[j] > now:
            num[j+1] = num[j]
        else:
            break
        j -= 1
    num[j+1] = now

print(num)