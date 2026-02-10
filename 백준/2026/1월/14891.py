import sys
from collections import deque
input = sys.stdin.readline
arr = [deque(map(int, list(input().strip()))) for _ in range(4)]
k = int(input())
move = [list(map(int, input().split())) for _ in range(k)]  # 번호, 방향
# 방향 = 1이면 시계방향, 방향 = -1이면 반시계

# 톱니바퀴 A를 회전할 때, 서로 맞닿은 극이 "다르면" 반대 방향으로 회전
# 0번 톱니 : 2번 (-> 1번 톱니)
# 1번 톱니 : 2번 (-> 2번 톱니), 6번 -> (0번 톱니)
# 2번 톱니 : 2번 (-> 3번 톱니), 6번 -> (1번 톱니)
# 3번 톱니 : 6번 (-> 2번 톱니)


def find_rotate_list(node, dir):  # 맞닿은 극 찾기
    rotate_list = [(node, dir)]
    now, now_dir = node, dir
    while 0 <= now+1 < 4 and arr[now][2] != arr[now+1][6]:
        rotate_list.append((now+1, -now_dir))  # node+1도 반대방향으로 회전
        now += 1
        now_dir = -now_dir
    while 0 <= node-1 < 4 and arr[node][6] != arr[node-1][2]:
        rotate_list.append((node-1, -dir))
        node -= 1
        dir = -dir
    return rotate_list


for idx, direction in move:
    idx -= 1
    rotate_list = find_rotate_list(idx, direction)
    for node, dir in rotate_list:
        arr[node].rotate(dir)

res = 0
for i in range(4):
    if arr[i][0] == 1:
        res += (2**i)
print(res)