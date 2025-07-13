n, m = map(int, input().split())
m_arr = list(map(int, input().split()))
c_arr = list(map(int, input().split()))

temp = [float('INF')] * (m+1)
for i in range(m+1):
    if i <= m_arr[0]:
        temp[i] = c_arr[0]

for i in range(1, n):
    dp = [float('INF')] * (m + 1)
    num = m_arr[i]
    value = c_arr[i]
    for j in range(m+1):
        if j <= num:
            dp[j] = min(temp[j], value)
        else:
            dp[j] = min(temp[j], temp[j-num] + value)
    temp = dp

if n == 1:
    print(c_arr[0])
else:
    print(dp[-1])