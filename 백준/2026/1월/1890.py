import sys

input = sys.stdin.readline
n = int(input())  # 4 ~ 100
arr = [list(map(int, input().split())) for _ in range(n)]
# 경로의 개수는 최대 2^63 -1 개.. -> 그냥 dfs로 풀었다간 죽음뿐. -> 그렇다면 필히 dp나 백트래킹으로 재귀를 줄여야겠네!
dx = [0, 1]  # 오른쪽, 아래
dy = [1, 0]
# dp 테이블에 뭘 저장할 수 있을까? = 언제 어떤 값을 재활용할 수 있을까?
memo = [[-1] * n for _ in range(n)]
# 1. dfs(0,0) 에서 시작.
# 2. 내가 갈 수 있는 곳은 오른쪽 m칸, 아래로 m 칸 총 두 곳이야!
# 3. 야 나에서 m칸 아래 너! 너에서 시작해서 목적지 도착하는 경로 몇개야! (dfs(xx, yy)호출)
# 4. 넵 저 k개 입니다!
# 5. 오키. 그럼 나는 그 2개의 k 다 합친거!


def dfs(x, y):
    if memo[x][y] != -1:  # 이미 방문한적 있는 곳
        return memo[x][y]
    if x == n-1 and y == n-1:
        return 1
    memo[x][y] = 0  # 일단 0으로 초기화
    m = arr[x][y]
    k = 0
    for i in range(2):
        xx, yy = x + (m*dx[i]), y + (m*dy[i])
        if 0 <= xx < n and 0 <= yy < n:
            # 오키 나 (xx, yy)로 점프 가능해! 야 (xx, yy) 너에서 시작하면 목적지까지 경로 몇개야?
            k += dfs(xx, yy)
    memo[x][y] = k
    return memo[x][y]


dfs(0, 0)
print(memo[0][0])