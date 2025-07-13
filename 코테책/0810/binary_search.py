def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
