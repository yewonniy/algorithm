n = int(input())

arr = list(map(int, input().split()))
memo = []

for i, num in enumerate(arr):
    memo.append((i, num))

arr_2 = sorted(set(arr))

for i in range(len(arr_2)):
    print(arr_2.index(memo[i][1]), end=' ')
