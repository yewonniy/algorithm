import sys
input = sys.stdin.readline
n = int(input())  # 2천
arr = list(map(int, input().split()))
m = int(input())  # 백만 -> O(nm)은 불가!!! -> dp?
dp = [[0] * n for _ in range(n)]  # 메모리 : 400만


def check(pt1, pt2):
    while (0 <= pt1) and (pt2 < n):
        if arr[pt1] != arr[pt2]:
            break
        else:
            dp[pt1][pt2] = 1
        pt1 -= 1
        pt2 += 1


for i in range(n):  # 200만 번 정도 반복
    dp[i][i] = 1
    check(i-1, i+1)
    check(i, i+1)

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])