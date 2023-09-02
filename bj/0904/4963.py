import sys
m, n = map(int, input().split())


def count(array, M, N):
    visited = []
    cnt = 0
    memo = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 1 and (i, j) not in visited:
                visited.append((i, j))
                print((i, j))
                ni = i
                nj = j
                if i-1 >= 0:
                    if array[i-1][j] == 1 and (i-1, j) not in visited:
                        visited.append((i-1, j))
                        memo = 1
                    if j - 1 >= 0:
                        if array[i - 1][j - 1] == 1 and (i-1, j-1) not in visited:
                            visited.append((i-1, j-1))
                            memo = 1
                    if j + 1 < M:
                        if array[i - 1][j + 1] == 1 and (i-1, j+1) not in visited:
                            visited.append((i-1, j+1))
                            memo = 1
                if i+1 < N:
                    if array[i+1][j] == 1 and (i+1, j) not in visited:
                        visited.append((i+1, j))
                        memo = 1
                    if j - 1 >= 0:
                        if array[i + 1][j - 1] == 1 and (i+1, j-1) not in visited:
                            visited.append((i+1, j-1))
                            memo = 1
                    if j + 1 < M:
                        if array[i+1][j + 1] == 1 and (i+1, j+1) not in visited:
                            visited.append((i+1, j+1))
                            memo = 1
                if j - 1 >= 0:
                    if array[i][j - 1] == 1 and (i, j - 1) not in visited:
                        visited.append((i, j - 1))
                        memo = 1
                if j + 1 < M:
                    if array[i][j + 1] == 1 and (i, j + 1) not in visited:
                        visited.append((i, j + 1))
                        memo = 1
                print(visited)
                if memo == 1:
                    cnt += 1
    return cnt


while n != 0 and m != 0:
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    result = count(arr, m, n)
    print(result)
    m, n = map(int, input().split())