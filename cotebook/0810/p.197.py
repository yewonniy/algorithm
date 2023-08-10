n = int(input())
items = list(map(int, input().split()))
items.sort()
m = int(input())
require = list(map(int, input().split()))


def binary_search(array, item, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if item == array[mid]:
        return True
    elif item < array[mid]:
        return binary_search(array, item, start, mid-1)
    else:
        return binary_search(array, item, mid+1, end)


for target in require:
    result = binary_search(items, target, 0, n-1)
    if not result:
        print('no', end=' ')
    else:
        print('yes', end=' ')
