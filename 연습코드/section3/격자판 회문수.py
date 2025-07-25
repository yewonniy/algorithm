graph = []
column = [[] for _ in range(7)]
res = 0


def check(arr):
    cnt = 0
    reverse_arr = arr[::-1]
    for j in range(3):
        if arr[j:j+5] == reverse_arr[2-j:7-j]:
            cnt += 1
    return cnt


for i in range(7):
    arr = list(map(int, input().split()))
    for k in range(7):
        column[k].append(arr[k])
    graph.append(arr)
    res += check(arr)

for i in range(7):
    res += check(column[i])
print(res)