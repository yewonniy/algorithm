n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

dp = [0] * (k+1)  # dp[i] = arr[0~i]를 이용해서 i를 만들 수 있는 경우의 수

for i in range(n):
    dp[0] = 1
    for j in range(arr[i], k+1):
        dp[j] += dp[j-arr[i]]
print(dp[k])
# 점화식 : (나만 써서 현재 숫자 'i' 만들기 = 1 or 0) + (이전까지 수 + 나 해서 만들기)
