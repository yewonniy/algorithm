import sys
n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline()))

sum = 0
p = k
cnt = 0
for i in range(n-1, -1, -1):
    if sum >= k:
        break
    if coins[i] <= k and sum < k:
        while p - coins[i] >= 0:
            sum += coins[i]
            cnt += 1
            p -= coins[i]

print(cnt)