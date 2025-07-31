n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x: x[0], reverse=True)

weight = arr[0][1]
cnt = 1
for i in range(1, n):
    if arr[i][1] > weight:
        cnt += 1
        weight = arr[i][1]

print(cnt)