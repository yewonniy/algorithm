num_list = list(map(int, input().split()))
sort = input()
choice_cnt = 0
k = 0

if sort == "오름차순":
    for i in range(len(num_list)//2):
        # 버블 정렬
        for j in range(len(num_list)-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
        k += 1
        if k < len(num_list):
            for x in num_list:
                print(x, end=' ')
            print()
        min_num = max(num_list) + 1
        # 선택 정렬
        for j in range(choice_cnt, len(num_list)-1):
            if num_list[j] < min_num:
                min_num = num_list[j]
                min_index = j
        num_list[choice_cnt], num_list[min_index] = num_list[min_index], num_list[choice_cnt]
        k += 1
        if k < len(num_list):
            for x in num_list:
                print(x, end=' ')
            print()
        choice_cnt += 1
else: # 내림 차순
    for i in range(len(num_list)//2):
        # 버블 정렬
        for j in range(len(num_list)-1):
            if num_list[j] < num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
        k += 1
        if k < len(num_list):
            for x in num_list:
                print(x, end=' ')
            print()
        max_num = min(num_list) - 1
        # 선택 정렬
        for j in range(choice_cnt, len(num_list)-1):
            if num_list[j] > max_num:
                max_num = num_list[j]
                max_index = j
        num_list[choice_cnt], num_list[max_index] = num_list[max_index], num_list[choice_cnt]
        k += 1
        if k < len(num_list):
            for x in num_list:
                print(x, end=' ')
            print()
        choice_cnt += 1