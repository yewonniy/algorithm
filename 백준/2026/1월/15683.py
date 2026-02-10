# 0 빈칸, 1~5 씨씨티비 유형 6 벽
# 사각지대의 최소 크기
import sys
from collections import defaultdict

input = sys.stdin.readline
n, m = map(int, input().split()) # 0 <= xx < n
arr = []
cctvs = defaultdict(list)
cnt = n*m  # 사각지대 수
cctv_zone = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if 1 <= tmp[j] <= 5:
            cctvs[tmp[j]].append((i, j))
            cnt -= 1
            cctv_zone.append(list())
        elif tmp[j] == 6:
            cnt -= 1
    arr.append(tmp)


def supervise_upside(x, y):
    tmp = set()
    for xx in range(x-1,-1,-1):
        if arr[xx][y] == 0:
            tmp.add((xx, y))
        if arr[xx][y] == 6:
            break
    return tmp
def supervise_right(x, y):
    tmp = set()
    for yy in range(y+1, m):
        if arr[x][yy] == 0:
            tmp.add((x, yy))
        if arr[x][yy] == 6:
                break
    return tmp
def supervise_down(x, y):
    tmp = set()
    for xx in range(x+1, n):
        if arr[xx][y] == 0:
            tmp.add((xx, y))
        if arr[xx][y] == 6:
            break
    return tmp
def supervise_left(x, y):
    tmp = set()
    for yy in range(y-1,-1,-1):
        if arr[x][yy] == 0:
            tmp.add((x, yy))
        if arr[x][yy] == 6:
            break
    return tmp


i = 0
for type in cctvs: # type = cctv 유형
    cctv = cctvs[type]
    # cnt - 감시 가능한 곳 개수
    for x, y in cctv:
        # 기본 (rotate 없이 기본 방향)
        up, right, down, left = supervise_upside(x, y), supervise_right(x, y), supervise_down(x, y), supervise_left(x,y)
        if type == 1:
            cctv_zone[i].append(up)
            cctv_zone[i].append(right)
            cctv_zone[i].append(down)
            cctv_zone[i].append(left)
        elif type == 2:
            cctv_zone[i].append(left.union(right))
            cctv_zone[i].append(up.union(down))
        elif type == 3:
            cctv_zone[i].append(up.union(right))
            cctv_zone[i].append(right.union(down))
            cctv_zone[i].append(down.union(left))
            cctv_zone[i].append(left.union(up))
        elif type == 4:
            cctv_zone[i].append(up.union(right).union(left))
            cctv_zone[i].append(right.union(down).union(up))
            cctv_zone[i].append(down.union(left).union(right))
            cctv_zone[i].append(left.union(up).union(down))
        else:
            cctv_zone[i].append(up.union(right).union(left).union(down))
        i += 1


def dfs(L):
    global res, answer
    if L == len(cctv_zone):
        unionSet = set()
        for i in range(len(res)):
            unionSet = unionSet.union(res[i])
        answer = max(answer, len(unionSet))
        return
    for i in range(len(cctv_zone[L])):
        res.append(cctv_zone[L][i])
        dfs(L+1)
        res.pop()


answer = -1
res = []
dfs(0)
print(cnt - answer)

