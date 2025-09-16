n, m = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n)) # 점수 시간
dy = [0] * (m+1)

for i in range(n):
    score = arr[i][0]
    t = arr[i][1]
    for j in range(m, -1, -1):
        if i == 0 and j >= t:
            dy[j] = score
        elif j >= t:
            dy[j] = max(dy[j], dy[j-t]+score)
print(dy[-1])
