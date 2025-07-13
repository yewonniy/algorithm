import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

memo = []
score = 0
n = int(input())
cnt = 0


def dp(i, prev, scores):
    global cnt
    cnt += 1
    if cnt == n:
        memo.append(scores)
    if cnt < n:
        line = list(map(int, input().split()))
        if prev == 0:
            dp(i+1, 0, scores+line[0])
            dp(i+1, 1, scores+line[1])
        if prev == 1:
            dp(i+1, 0, scores + line[0])
            dp(i+1, 1, scores + line[1])
            dp(i+1, 2, scores + line[2])
        if prev == 2:
            dp(i + 1, 1, scores + line[1])
            dp(i + 1, 2, scores + line[2])


l = list(map(int, input().split()))
dp(1, 0, l[0])
dp(1, 1, l[1])
dp(1, 2, l[2])
print(memo)
print(max(memo), min(memo))