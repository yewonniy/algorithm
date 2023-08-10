n = int(input())

num = []
for i in range(n):
    num.append(int(input()))

nm = sorted(num, reverse=True)

for i in range(1, n):
    cur_index = i
    for j in range(i, -1, -1):
        if num[j] < num[cur_index]:
            num[j], num[cur_index] = num[cur_index], num[j]
            cur_index = j


print(num)
for i in nm:
    print(i, end=' ')