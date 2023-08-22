import sys
n = int(input())
arr = []

# n은 계단 갯수 (0 ~ n-1)
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.reverse()

# memo[i] -> i 번째 계단 까지 최대 점수. idx 번째 계단 에서의 최대 점수 계산
memo = [0]
memo[0] = arr[0]


def step(array, cnt, idx, his):
    global memo
    cnt += array[idx]
    if his == 1:
        if idx + 2 < n:
            step(array, cnt, idx + 2, 2)
    else:
        if idx + 1 < n:
            step(array, cnt, idx + 1, 1)
        if idx + 2 < n:
            step(array, cnt, idx + 2, 2)
    if idx == len(array) - 1:
        memo.append(cnt)
        memo.remove(min(memo))


if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] + arr[1])
elif n == 3:
    print(max(arr[0] + arr[1], arr[0] + arr[2]))
else:
    step(arr, arr[0], 1, 1)
    step(arr, arr[0], 2, 2)
    print(max(memo))