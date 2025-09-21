n = int(input())
arr = list(map(int, input().split()))
mini = float('inf')
res = [arr[0], arr[1]]

start = 0
end = n-1
while True:
    if start >= end:
        break
    s = arr[start] + arr[end]
    if abs(s) < mini:
        mini = abs(s)
        res = [arr[start], arr[end]]
    if s < 0:
        start += 1
    elif s > 0:
        end -= 1
    else:
        break
print(res[0], res[1])
