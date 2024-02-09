import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

memo = []


def dp(start, array, i, score):
    now = start
    if i == n:
        if score not in memo:
            memo.append(score)
    if i < n:
        score += array[i][now]
        if now == 0:
            dp(0, array, i+1, score)
            dp(1, array, i+1, score)
        if now == 1:
            dp(0, array, i+1, score)
            dp(1, array, i+1, score)
            dp(2, array, i+1, score)
        if now == 2:
            dp(1, array, i + 1, score)
            dp(2, array, i + 1, score)


max_ = 0
min_ = float("INF")

for i in range(0, 3):
    dp(i, arr, 0, 0)
    max_ = max(max_, max(memo))
    min_ = min(min_, min(memo))
    memo = []

print(max_, min_)