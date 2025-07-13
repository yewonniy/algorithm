import sys
move = [[0, -1], [0, 1], [-1, 0], [1, 0]]
sys.setrecursionlimit(100000)


def dfs(array, start):
    array.remove(start)
    for i in range(0, 4):
        nx = start[0] + move[i][0]
        ny = start[1] + move[i][1]
        if (nx >= 0) and (nx <= m-1) and (ny >= 0) and (ny <= n-1):
            new = [nx, ny]
            if new in array:
                dfs(array, new)
    return 1


t = int(input())
for _ in range(0, t):
    arr = []
    m, n, k = map(int, input().split())
    cnt = 0
    for i in range(k):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    while len(arr) > 0:
        cnt += dfs(arr, arr[0])
        if len(arr) <= 0:
            break
    print(cnt)