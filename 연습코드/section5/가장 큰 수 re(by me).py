n, k = input().split()
num = list(map(int, n))
k = int(k)

maxi = 0
index = 0
for i in range(k+1):
    if num[i] > maxi:
        index = i
        maxi = num[i]
for i in range(index):
    num.pop(0)
    k -= 1

while k > 0:
    if k == 0:
        break
    for i in range(len(num)-1):
        if num[i] < num[i+1]:
            num.pop(i)
            k -= 1
            break
    else:
        break

for _ in range(k):
    num.pop()
print(num)