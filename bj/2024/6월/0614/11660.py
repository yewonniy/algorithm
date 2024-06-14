n, m = map(int, input().split())
arr = []
memo = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    memo.append([0] * n)
memo[0][0] = arr[0][0]

for y in range(1, n):
    memo[0][y] = memo[0][y - 1] + arr[0][y]  # 첫줄 완성

for x in range(1, n):  # 두번째 줄부터 마지막 줄까지 채우기
    cnt = 0
    for y in range(n):
        cnt += arr[x][y]
        memo[x][y] = memo[x-1][y] + cnt

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 1 and y1 == 1:
        print(memo[x2-1][y2-1])
    elif x1 == 1:
        print(memo[x2-1][y2-1] - memo[x2-1][y1-2])
    elif y1 == 1:
        print(memo[x2-1][y2-1] - memo[x1-2][y2-1])
    else:
        print(memo[x2-1][y2-1] - memo[x2-1][y1-2] - memo[x1-2][y2-1] + memo[x1-2][y1-2])