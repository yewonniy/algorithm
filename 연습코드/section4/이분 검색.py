n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


def binary_search(arr, start, end, target):
    mid = (start + end)//2
    if start > end:
        return -1
    if arr[mid] == target:
        return mid + 1
    elif arr[mid] > target:
        return binary_search(arr, start, mid, target)
    else:
        return binary_search(arr, mid, end, target)


print(binary_search(arr, 0, n-1,  m))
