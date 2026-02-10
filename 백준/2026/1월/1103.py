# 1. 동전이 멈췄을 때 위치가 H 거나
# 2. 동전이 격자 밖으로 나가면 종료
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
H = 'H'
for _ in range(n):
    tmp = list(input().rstrip())
    for i, x in enumerate(tmp):
        if x.isdigit():
            tmp[i] = int(x)
    arr.append(tmp)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 문제 1: 무한번 움직일 수 있다면 -1을 출력. -> 사이클을 어떻게 찾지?
# 그냥 dfs로 안 풀려? 왜? 격자의 크기가 최대 2,500밖에 안되는데?
memo = [[-1] * m for _ in range(n)] # 방문했는데 갈 방향이 없으면 0 (갈 수 있는 방향의 개수를 저장한다)
stack = [[False] * m for _ in range(n)]


# 1. 야 (x, y)에서 시작해서 최대 몇 번이나 움직일 수 있냐?
# 2. 일단 나는 0개의 방향으로 이동할 수 있다고 초기화 해놓고, 한 방향이라도 가능하면 1로 초기화
# 3. 야 나에서 갈 수 있는 (xx, yy) 너에서 시작하면 몇번 움직이냐?
# 4. 넵 저 k 번 움직일 수 있습니다.
# 5. 오키 그럼 난 1 + max(k)!
def dfs(x, y):
    # 난제 : 사이클 찾기 (발견 즉시 -1 리턴하고 프로그램 종료)
    # 사이클 : 아직 재귀가 안끝난, 스택에 있는 (xx, yy)를 내가 방문 가능한 경우
    # x, y를 받았는데 얘가 스택에 있는 애네? -> -1 리턴. 어떻게 구현할 것이냐. -> 현재 스택에서 재귀ing인 놈인지 판단하는 그래프 추가
    if stack[x][y]:
        # 사이클
        return -2
    if memo[x][y] != -1:
        return memo[x][y]
    stack[x][y] = True
    memo[x][y] = 0
    k = 0
    for i in range(4):
        xx, yy = x+(arr[x][y]*dx[i]), y+(arr[x][y]*dy[i])
        if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] != H:
            # if k == 0:
            #     k = 1 # 일단 1칸은 이동 가능
            res = dfs(xx, yy)
            if res == -2: return -2
            k = max(k, 1 + res) # 내가 xx, yy로 간 1칸 이동 + (xx, yy)에서 출발했을 때 최대 버티는 수
    memo[x][y] = k
    stack[x][y] = False # 재귀 끝
    return k


res = dfs(0, 0)
print(res+1)

