n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))

res = 0
for i in range(n//2+1):
    for j in range(n // 2 - i, n // 2 + i + 1):
        res += arr[i][j]
        if i != n//2:
            res += arr[-i-1][j]

print(res)