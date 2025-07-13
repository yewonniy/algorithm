num = list(map(int, input().split()))

for i in range(0, len(num)-1):
    sub_list = num[i:len(num)]
    min_num = min(sub_list)
    min_index = num.index(min_num)
    num[min_index] = num[i]
    num[i] = min_num
    
print(num)