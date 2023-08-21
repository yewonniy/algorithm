import sys
n = int(input())
arr = []

for i in range(n):
    arr.append(map(int, sys.stdin.readline().rstrip()))
arr.reverse()
memo = [0] * (n+1)
his = [0] * (n+1)


def jump(array, idx, cnt, history):
    global memo
    history.append(idx)
    for i in range(1, len(array)):
        if len(history) > 1:
            if history[-1] - history[-2] == 1:
                jump(array, idx+2, cnt+array[idx+2], history)
            else:
        else:
            memo[idx] = jump(array, idx+1, cnt+array[idx+1], history)
            jump(array, idx+2, cnt+array[idx+2], history)


jump(arr, 0, arr[0], his)

print(max(memo))