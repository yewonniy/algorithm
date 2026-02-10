import sys
sys.setrecursionlimit(10**9)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]  # 시간, 금액 순
# Top - down
res = 0


def top_down(now):
    # 야 나 date일째인데, 나 다음에 일할 수 있는 너! date+arr[date][0] 너!
    # 너에서 value 최대값 뭐야!
    # 예 저 k입니다
    # ok그럼 난 k+value
    cost, value = arr[now]
    if dp[now] != -1:
        return dp[now]
    next_node = now + cost
    if next_node < n:
        k = 0
        while next_node < n:
            k = max(k, top_down(next_node))
            next_node += 1
        dp[now] = k + value
    elif next_node == n:
        # 하고 끝!
        dp[now] = value
    else: # now 꺼는 못함.
        dp[now] = 0
    return dp[now]


dp = [-1] * n
for i in range(n):
    res = max(res, top_down(i))
print(res)

dp = [0] * (n+1)
# 오늘 상담 해? 말아?
for i in range(n-1, -1, -1): # n-1 ~ 0까지
    cost, value = arr[i]
    if i + cost > n: # 못함
        dp[i] = dp[i+1]
    else: # 오늘 할 수 있음 -> 해 말아 선택
        dp[i] = max(dp[i+1], dp[i+cost] + value)
print(dp)