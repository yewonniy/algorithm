from itertools import combinations
n, m = map(int, input().split())

arr = []
for i in range(1, n+1):
    arr.append(i)

if m > 1:
    if n != m:
        result = list(combinations(arr, m))
        for x in result:
            for a in x:
                print(a, end=' ')
            print()
    else:
        for x in arr:
            print(x, end=' ')
else:
    for x in arr:
        print(x)