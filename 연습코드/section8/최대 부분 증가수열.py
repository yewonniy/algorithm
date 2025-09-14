n = int(input())
arr = list(map(int, input().split()))
memo = [0] * n
memo[0] = 1
for i in range(1, n):
    maxi = 1
    for j in range(i):
        if arr[i] > arr[j]:
            maxi = max(memo[j]+1, maxi)
    memo[i] = maxi

print(max(memo))