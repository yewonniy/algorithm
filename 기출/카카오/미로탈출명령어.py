import sys
sys.setrecursionlimit(200000)
answer = []


def dfs(L, x, y, target_x, target_y, n, m, k, res):
    global answer
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    path = ['d', 'l', 'r', 'u']
    if len(answer) > 0:  # 조기 리턴
        return
    if L == k:
        if x == target_x and y == target_y:
            print(res)
            answer.append(res)
        return
    if abs(target_x - x) + abs(target_y - y) > k - L or (
            k - L - (abs(target_x - x) + abs(target_y - y))) % 2 == 1:  # 조기리턴
        return
    for i in range(4):
        if 0 <= x + dx[i] <= n and 0 <= y + dy[i] <= m:
            dfs(L + 1, x + dx[i], y + dy[i], target_x, target_y, n, m, k, res + path[i])


def solution(n, m, x, y, r, c, k):
    global answer
    dfs(0, x - 1, y - 1, r - 1, c - 1, n - 1, m - 1, k, '')
    if len(answer) > 0:
        return answer[0]
    return "impossible"