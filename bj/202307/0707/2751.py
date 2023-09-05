n= int(input())
num_list = list()
new_list = list()

for i in range(0, n):
    num_list.append(None)
    num = int(input())
    num_list[i] = num

new_list = sorted(num_list)
print(new_list)
for i in range(0, n):
    print(new_list[i], end="\n")