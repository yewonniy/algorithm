import sys
n, m = map(int, input().split())
arr = list(map(int, input().split()))
memo = [0] * 100001
memo[1] = arr[0]


def add(array, index):
    global memo
    result = 0
    if index == 0:
        return 0
    if memo[index] != 0:
        return memo[index]
    else:
        for i in range(index, 0, -1):
            if memo[i] != 0:
                for j in range(i, index):
                    result += array[j]
                memo[index] = memo[i] + result
                return memo[index]


for i in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    print(add(arr, end)-add(arr, start-1))
