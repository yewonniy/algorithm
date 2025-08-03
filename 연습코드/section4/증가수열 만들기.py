from collections import deque

n = int(input())
arr = deque(map(int, input().split()))

num = -1
res = ""
cnt = 0
while arr:
    if num < arr[0] < arr[-1] or (arr[-1] <= num < arr[0]):
        num = arr[0]
        arr.popleft()
        res += "L"
        cnt += 1
    elif num < arr[-1] < arr[0] or (arr[0] <= num < arr[-1]):
        num = arr[-1]
        arr.pop()
        res += "R"
        cnt += 1
    else:
        break
print(cnt)
print(res)