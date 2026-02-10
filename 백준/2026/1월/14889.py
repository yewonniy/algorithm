from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())  # 4 ~ 20
arr = []  # arr[i][j] + arr[j][i]
for _ in range(n):
    arr.append(list(map(int, input().split())))
res = float("inf")  # 능력치 차이의 최소값

team_s = list(combinations(range(n), n//2))
team_l = team_s[len(team_s)//2:][:]
for i in range(len(team_s)//2):
    s = team_s[i]
    l = team_l[-(i+1)]
    start = 0  # 스타트 팀의 총 능력치
    link = 0  # 링크 팀의 총 능력치
    for idx1 in range(n//2):
        for idx2 in range(idx1+1, n//2):
            start += (arr[s[idx1]][s[idx2]] + arr[s[idx2]][s[idx1]])
            link += (arr[l[idx1]][l[idx2]] + arr[l[idx2]][l[idx1]])
    res = min(res, abs(start-link))
print(res)
