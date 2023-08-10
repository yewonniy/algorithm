n = int(input())
people_list = list()

for i in range(0, n):
    a, b = input().split()
    people_list.append([int(a), b])

sorted_list = sorted(people_list, key=lambda x: x[0])

for i in range(0, n):
    print(sorted_list[i][0], sorted_list[i][1])