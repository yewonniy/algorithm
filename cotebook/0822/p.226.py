n, m = map(int, input().split())

arr = []

# memo[i] -> i 원을 만드는 데 쓰이는 동전의 최소 갯수
memo = [789456132] * (m + 1)

for i in range(n):
    arr.append(int(input()))
    if arr[i] < m + 1:
        memo[arr[i]] = 1

for i in range(m + 1):
    for j in range(0, n):
        if (i - arr[j] > 0) and (i - arr[j] < m + 1):
            memo[i] = min(memo[i], memo[i - arr[j]] + 1)

if memo[m] < 789456132:
    print(memo[m])
else:
    print(-1)
