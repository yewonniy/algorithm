n, m = map(int, input().split())
rice = list(map(int, input().split()))

rice.sort(reverse=True)
length_memory = [(2000000000, 2000000000)]
print(rice)

def binary_search(array, start, end, target):
    mid = (start + end) // 2
    length = 0 # 잘리는 떡의 길이
    global length_memory
    if start < end:
        # 최선의 답 고르기
        return 0
    for i in array:
        if i > mid:
            length += (i - mid)
        else:
            break
    if length < target: # 더 잘라야 함
        return binary_search(array, mid-1, end, target)
    elif length > target: # 덜 잘라야 함
        length_memory.append((length, mid))
        return binary_search(array, start, mid+1, target)
    else: # 딱 떨어지는 답
        return mid


result = binary_search(rice, rice[0], 0, m)
if result == 0:
    length_memory.sort(key=lambda data: data[0])
    print(length_memory)
    result = length_memory[0][1]
print(result)