# i번 세로선의 결과 = i
# 사다리는 인접하게 놓을 수 없음
import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())  # n: 가로(10), h: 세로(30), m: 사다리의 개수
graph = [[0] * (n+1) for _ in range(h+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
ans = 4


# 1. 사다리 타고 내려가기 구현
def check():
    for start in range(1, n+1):
        now = start
        for x in range(1, h+1):
            if graph[x][now] == 1:
                now += 1
            elif now > 1 and graph[x][now-1] == 1:
                now -= 1
        if start != now:
            return False
    return True


# 2. 사다리 놓기 (백트래킹)
def dfs(target_depth, cnt, x, y):
    global ans
    if cnt >= ans:
        return
    if cnt == target_depth:
        if check():
            ans = min(ans, cnt)
            return True
        return
    for i in range(x, h+1):
        k = y if i == x else 1
        for j in range(k, n):
            if not graph[i][j] and not graph[i][j-1] and not graph[i][j+1]:
                graph[i][j] = 1
                if dfs(target_depth, cnt+1, i, j+2):
                    return True
                graph[i][j] = 0


for i in range(4):
    if dfs(i, 0, 1, 1):
        break
print(ans if ans <= 3 else -1)