# 정수 삼각형 dfs?
n = int(input())
triangle = []
for _ in range(n):
    arr = list(map(int, input().split()))
    triangle.append(arr)
maxi = -1


def dfs(level, total, index):
    global maxi
    if level == n:
        maxi = max(maxi, total)
    else:
        if index+1 < n:
            for i in range(index, index+2):  # 다음 층은 같은 인덱스, 혹은 인덱스+1로만 이동 가능
                dfs(level+1, total + triangle[level][index], i)
        else:
            dfs(level+1, total+triangle[level][index], index)


dfs(0, 0, 0)
print(maxi)