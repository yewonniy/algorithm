n = int(input())
num_list = (input()).split()

for i in range(0, n):
    num_list[i] = int(num_list[i])

num_list = sorted(num_list)

m = int(input())
m_list = (input()).split()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


for i in range(0,m):
    m_list[i] = int(m_list[i])
    result = binary_search(num_list, m_list[i], 0, len(num_list)-1)
    if result is None:
        print(0)
    else:
        print(1)


