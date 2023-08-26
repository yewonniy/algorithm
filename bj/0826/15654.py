from itertools import permutations
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = list(permutations(arr, m))
for x in result:
    for a in x:
        print(a, end=' ')
    print()