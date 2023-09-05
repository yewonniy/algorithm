N = int(input())
num_list = list()

sum = 0.0

for i in range(0, N):
    m = int(input())
    num_list.append(m)
    sum += float(num_list[i])

num_ = num_list.copy()
while len(num_) != 0:
    for i, num in enumerate(set(num_)):
        num_.remove(num)
    if i == 0:
        popular = num
    else:
        popular = num_list[0]

print(round(sum/float(N)))
num_list.sort()
print(num_list[N//2])
print(popular)
print(num_list[N-1]-num_list[0])