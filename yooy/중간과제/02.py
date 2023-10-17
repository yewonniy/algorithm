import copy
n = int(input())

memo = [[1],[2],[1,2]]
array = [i for i in range(1, n+1)]


def append_(arr, num):
    new = copy.deepcopy(arr)
    new.append(num)
    return new


for i in range(2, n): # i = 2
    for j in range(0, len(memo)): # j = 0,1,2
        new_arr = append_(memo[j], array[i])
        memo.append(new_arr)

max_n = 0
for x in memo:
    if sum(x) == n:
        max_n = max(max_n, len(x))
        print(x, max_n)