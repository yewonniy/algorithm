N = int(input())
num_list = list()

sum = 0.0

for i in range(0, N):
    m = int(input())
    num_list.append(m)
    sum += float(num_list[i])
print(num_list)

cnt_num = []
for i in num_list:
    cnt = num_list.count(i)



print(round(sum/float(N)))
num_list.sort()
print(num_list[N//2])
print("최빈값")
print(num_list[N-1]-num_list[0])