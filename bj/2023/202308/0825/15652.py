from itertools import combinations
n, m = map(int, input().split())

arr = []
for i in range(1, n+1):
    arr.append(i)
arr.extend(arr * (m-1))
arr.sort()

if m == 1:
    for i in range(1, n+1):
        print(i)
else:
    result = list(set(combinations(arr, m)))
    result.sort()
    for x in result:
        for a in x:
            print(a, end=' ')
        print()