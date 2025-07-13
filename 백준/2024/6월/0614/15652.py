n, m = map(int,input().split())
# 1부터 n 까지 m개를 고른 수열 (중복 가능)
arr = []


def dfs(level, num):
    arr.append(num)
    if level == m:
        for j in range(m):
            print(arr[j+1], end=' ')
        print()
    else:
        for i in range(num, n+1):
            dfs(level+1, i)
            arr.pop()


dfs(0, 1)