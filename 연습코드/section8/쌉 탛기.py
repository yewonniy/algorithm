n = int(input())
arr = []
for i in range(n):
    width, height, weight = map(int, input().split())
    arr.append([width, weight, height]) # 넓이, 높이, 무게
arr.sort(key=lambda x:x[0], reverse=True)

memo = [0] * n
memo[0] = arr[0][2]
for i in range(1, n):
    w = arr[i][2]
    for j in range(i):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            w = max(w, memo[j] + arr[i][2])
    memo[i] = w
print(max(memo))