n = int(input())

arr = list(map(int, input().split()))
arr_2 = sorted(set(arr))


def binary_search(array, target, start, end):
    mid = (start + end)//2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


for i in range(n):
    result = binary_search(arr_2, arr[i], 0, len(arr_2)-1)
    print(result, end=' ')