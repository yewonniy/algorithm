t = int(input()) # 지폐 금액
k = int(input()) # 동전 종류 수
coins = []
for _ in range(k):
    a, b = map(int, input().split())
    coins.append((a, b))
cnt = 0


def dfs(L, sum):
    global cnt
    if sum == t:
        cnt += 1
        return
    if sum > t or L >= k:
        return
    for i in range(coins[L][1]+1):
        dfs(L+1, sum+(coins[L][0] * i))


dfs(0, 0)
print(cnt)