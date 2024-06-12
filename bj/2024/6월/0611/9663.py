#  N-Queen 문제
n = int(input())
cnt = 0


def dfs(level, index):
    global cnt
    for j in range(1, n-level): # 대각선 check
        check[level+j][index] += 1
        if index + j < n and level + j < n:
            check[level+j][index+j] += 1
        if index - j >= 0 and level + j < n:
            check[level+j][index-j] += 1
    if level == n-1:
        cnt += 1
    else:
        for i in range(n):
            if check[level+1][i] < 1:
                dfs(level+1, i)
        for j in range(1, n - level):  # 대각선 check
            check[level + j][index] -= 1
            if index + j < n and level + j < n:
                check[level + j][index + j] -= 1
            if index - j >= 0 and level + j < n:
                check[level + j][index - j] -= 1


for i in range(n):
    check = []
    for _ in range(n):
        check.append([0] * n)  # 1 이상이면 못 들어가는 인덱스
    dfs(0, i)
print(cnt)