n = int(input())
arr = list(map(int, input().split()))
m = int(input())
dy = [9999999] * (m+1)
dy[0] = 0
for i in range(n):
    coin = arr[i]
    for j in range(coin, m+1):
        dy[j] = min(dy[j], dy[j-coin] + 1)
print(dy[-1])