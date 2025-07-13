n, m = map(int, input().split())
data = list(map(int, input().split()))
cnt_memory = []


def binary_search(array, start, end, target):
    cnt = 0
    global cnt_memory
    if start > end:
        cnt_memory.sort(key=lambda datas: datas[0])
        return cnt_memory[0][1]
    mid = (start + end) // 2
    for i in range(len(array)):
        if array[i] > mid:
            cnt += (array[i] - mid)
    if cnt == target:
        return mid
    elif cnt > target: # cnt가 가장 작은 게 정답일 수 있음
        cnt_memory.append((cnt, mid))
        return binary_search(array, mid + 1, end, target)
    else:
        return binary_search(array, start, mid - 1, target)


result = binary_search(data, 0, max(data)-1, m)
print(result)