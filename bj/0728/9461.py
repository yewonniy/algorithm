T = int(input())

for i in range(T):
    N = int(input())
    if N==1 or N==2 or N==3:
        print(1)
    elif N==4 or N==5:
        print(2)
    else:
        num_list = [1, 1, 1, 2, 2]
        for j in range(N-5):
            temp = num_list[0] + num_list[4]
            num_list[0] = num_list[1]
            num_list[1] = num_list[2]
            num_list[2] = num_list[3]
            num_list[3] = num_list[4]
            num_list[4] = temp
        print(num_list[4])

