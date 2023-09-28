import sys
n, k = map(int, input().split())
arr = []
for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    if w <= k:
        arr.append((w, v)) # 무게, 가치 순
memo = []
arr.sort()


def dp(array, start, w_sum, v_sum, w_, v_):
    global k
    w_sum += w_
    v_sum += v_
    if w_sum <= k:
        memo.append(v_sum)
    for i in range(1, len(arr)-start):
        dp(arr, start+i, w_sum, v_sum, arr[start+i][0], arr[start+i][1])


for i in range(len(arr)):
    dp(arr, i, 0, 0, arr[i][0], arr[i][1])
print(max(memo))