num = list(map(int, input().split()))

for i in range(1, len(num)+1):
    cnt = 0 # 1이면 한 개라도 swap 한거
    for j in range(0, len(num)-i):
        if num[j] > num[j+1]:
            cnt = 1
            num[j], num[j+1] = num[j+1], num[j]
    if cnt == 0:
        break

print(num)
