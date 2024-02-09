import sys
sys.setrecursionlimit(10000)

m, n = map(int, input().split())


def direction(array, i, j, cnt, M, N, visited):
    ni = i
    nj = j
    if i - 1 >= 0:
        if array[i - 1][j] == 1 and (i - 1, j) not in visited:
            visited.append((i - 1, j))
            if i-1 > 0:
                ni = i-1
                direction(array, ni, nj, cnt, M, N, visited)
        if j - 1 >= 0:
            if array[i - 1][j - 1] == 1 and (i - 1, j - 1) not in visited:
                visited.append((i - 1, j - 1))
                if i - 1 > 0 or j - 1> 0:
                    ni = i-1
                    nj = j-1
                    direction(array, ni, nj, cnt, M, N, visited)
        if j + 1 < M:
            if array[i - 1][j + 1] == 1 and (i - 1, j + 1) not in visited:
                visited.append((i - 1, j + 1))
                ni = i-1
                nj = j+1
                direction(array, ni, nj, cnt, M, N, visited)
    if i + 1 < N:
        if array[i + 1][j] == 1 and (i + 1, j) not in visited:
            visited.append((i + 1, j))
            ni = i+1
            nj = j
            direction(array, ni, nj, cnt, M, N, visited)
        if j - 1 >= 0:
            if array[i + 1][j - 1] == 1 and (i + 1, j - 1) not in visited:
                visited.append((i + 1, j - 1))
                ni = i+1
                nj = j-1
                direction(array, ni, nj, cnt, M, N, visited)
        if j + 1 < M:
            if array[i + 1][j + 1] == 1 and (i + 1, j + 1) not in visited:
                visited.append((i + 1, j + 1))
                ni = i+1
                nj = j+1
                direction(array, ni, nj, cnt, M, N, visited)
    if j - 1 >= 0:
        if array[i][j - 1] == 1 and (i, j - 1) not in visited:
            visited.append((i, j - 1))
            ni = i
            nj = j-1
            direction(array, ni, nj, cnt, M, N, visited)
    if j + 1 < M:
        if array[i][j + 1] == 1 and (i, j + 1) not in visited:
            visited.append((i, j + 1))
            ni = i
            nj = j+1
            direction(array, ni, nj, cnt, M, N, visited)
    return 1


def count(array, M, N):
    visited = []
    cnt = 0
    memo = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 1 and (i, j) not in visited:
                visited.append((i, j))
                cnt += direction(array, i, j, cnt, M, N, visited)
    return cnt


while n != 0 and m != 0:
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    result = count(arr, m, n)
    print(result)
    m, n = map(int, sys.stdin.readline().rstrip().split())