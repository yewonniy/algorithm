# n * n 땅
# m개의 나무를 심음
import sys
from collections import defaultdict
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[5] * n for _ in range(n)]
arr = [list(map(int, input().split())) for _ in range(n)]  # n = 1~10
tree = defaultdict(list) # 키: 나무의 좌표, value : 나무의 나이
for _ in range(m):
    x, y, age = map(int, input().split())
    tree[(x-1, y-1)].append(age)
for key in tree:
    tree[key].sort()

dx = [0,1,0,-1, 1,1,-1,-1]
dy = [1,0,-1,0, -1,1,-1,1]

# 처음 : 모든 칸에 5만큼의 양분
# 봄 : 자기 나이만큼의 양분을 먹고 나이 += 1 (나이 어린 애부터 먹고 못 먹는 애부터 다 죽어)
# 여름 : 죽은 나무 // 2 만큼 양분 추가
# 가을 : 나이 % 5 == 0 이면 번식 (인접 8개 칸에 나이 1인 나무 생김)
# 겨울 : (r, c)에 arr[r][c] 만큼의 양분 추가 (모든 칸에 추가)
# 위 과정을 k 번 반복 (최대 1,000번)
for _ in range(k):
    # 1. 봄
    for cor in tree: # cor : (x,y)
        x, y = cor
        new, death = [], []
        for age in tree[cor]:
            if graph[x][y] >= age:  # 양분 먹을 수 있음
                graph[x][y] -= age  # 양분 먹은 만큼 빼고,
                new.append(age+1)  # 나이 1살 추가하기
            else:  # 양분 못먹으면
                death.append(age)  # 죽은 나무에 나이 추가
        tree[cor] = new  # 양분 먹은 애들로만 교체

        # 2. 여름 graph[x][y]에 death//2
        for age in death:
            graph[x][y] += int(age//2)

    # 3. 가을 (번식)
    new = []
    for cor in tree:
        x, y = cor
        for age in tree[cor]:
            if age % 5 == 0:  # 5의 배수이면
                for i in range(8):
                    xx, yy = x+dx[i], y+dy[i]
                    if 0 <= xx < n and 0 <= yy < n:
                        new.append((xx, yy))  # 인접 8곳에 나이 1인 나무 추가
    if new:
        for x, y in new:
            tree[(x, y)].append(1)
    for cor in tree:
        tree[cor].sort()  # 정렬

    # 4. 겨울 (양분 추가)
    for x in range(n):
        for y in range(n):
            graph[x][y] += arr[x][y]

ans = 0
for cor in tree:
    ans += len(tree[cor])
print(ans)