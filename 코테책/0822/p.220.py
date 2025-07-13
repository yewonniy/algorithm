n = int(input())
arr = list(map(int, input().split()))

memo = [0] * (n+1)
memo[1] = arr[0]

# memo[i] -> arr[i-1] 번째 까지 턴 것의 최대값
for i in range(1, n+1):
    for k in range(2, i+1):
        if i-k <= n:
            memo[i] = max(memo[i], memo[i-k] + arr[i-1])
print(memo)

# 책 에서의 풀이
memo = [0] * (n+1)
memo[0] = arr[0]
memo[1] = max(memo[0], arr[1])

for i in range(2, n):
    memo[i] = max(memo[i-1], memo[i-2] + arr[i])

print(memo)

print(max(memo))