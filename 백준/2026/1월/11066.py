import sys
input = sys.stdin.readline
t = int(input())  # 테스트 케이스 개수
for _ in range(t):
    n = int(input())  # 총 파일 개수 (500)
    arr = list(map(int, input().split()))

    dp = [[float('inf')] * n for _ in range(n)]
    S = [0] * (n+1)
    for i in range(n):
        dp[i][i] = 0
        S[i+1] += S[i] + arr[i]
    for bunch in range(1, n):
        for i in range(n-bunch):
            j = i + bunch
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j])
            dp[i][j] += (S[j+1]-S[i])
    print(dp[0][n-1])

