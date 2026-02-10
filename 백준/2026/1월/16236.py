import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = []
for x in range(n):
    tmp = list(map(int, input().split()))
    for y, fish_size in enumerate(tmp):
        if fish_size == 9:
            shark_pos = [x, y]
            tmp[y] = 0
    arr.append(tmp)

dx = [-1, 0, 1, 0]  # 위, 왼, 아래, 우
dy = [0, -1, 0, 1]


def cal_distance():
    # bfs
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((0, shark_pos[0], shark_pos[1]))
    min_distance = float('inf')
    candidate = []
    while q:
        dis, x, y = q.popleft()
        if dis < min_distance:
            for i in range(4):
                xx, yy = x + dx[i], y + dy[i]
                if 0 <= xx < n and 0 <= yy < n and arr[xx][yy] <= shark_size and not visited[xx][yy]:  # 상어 사이즈 이하만 지나갈 수 있음
                    if 0 < arr[xx][yy] < shark_size:
                        min_distance = dis+1
                        candidate.append((xx, yy))
                    q.append((dis+1, xx, yy))
                    visited[xx][yy] = True
        elif dis == min_distance:
            if 0 < arr[x][y] < shark_size:
                candidate.append((x, y))
    if len(candidate) == 0:
        return (0, 0, 0)
    answer = [float('inf'), float('inf')]
    for x, y in candidate:
        if answer[0] > x:
            answer = [x, y]
        elif answer[0] == x and answer[1] > y:
            answer = [x, y]
    return (min_distance, answer[0], answer[1])


shark_size = 2
eating_cnt = 0
time = 0
while True:
    idx = []
    distance, next_x, next_y = cal_distance()
    time += distance
    if distance == 0:  # = 먹을 수 있는 물고기가 없단 뜻
        print(time)
        break
    shark_pos = [next_x, next_y]  # 상어 -> 먹은 물고기 위치로 이동
    arr[next_x][next_y] = 0  # 물고기 먹은 곳은 빈칸으로
    eating_cnt += 1  # 먹은 물고기 수 += 1
    if eating_cnt == shark_size and shark_size < 7:
        shark_size += 1
        eating_cnt = 0

# 1. m 마리의 물고기
# 2. 상어 크기 = 2
# 3. 물고기 크기 = 1~6
# 3. 물고기 > 상어 -> 지나갈 수 X, 먹을 수 X
# 4. 물고기 = 상어 -> 지나갈 수 O, 먹을 수 X
# 5. 물고기 < 상어 -> 지나갈 수 O, 먹을 수 O
# 6. 먹을 수 있는 물고기가 1 마리 -> 걔 먹으러 ㄱㄱ
# 7. 여러 마리 -> 가장 가까운 물고기. (가장 위쪽 / 가장 왼쪽 순)
# 8. 크기 만큼의 물고기를 먹으면 크기 +1
# 9. 더 이상 먹을 수 있는 물고기가 없으면 끝