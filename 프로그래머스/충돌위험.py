from collections import deque


def solution(points, routes):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    a = []
    l = 0
    for i in range(len(routes)):
        route = routes[i]
        dir = 0
        res = []
        for j in range(len(route) - 1):
            if j == 0:
                res.append([points[route[j] - 1][0], points[route[j] - 1][1]])
            q = deque()
            q.append([points[route[j] - 1][0], points[route[j] - 1][1]])
            target_x = points[route[j + 1] - 1][0]
            target_y = points[route[j + 1] - 1][1]
            while q:
                x, y = q.popleft()

                if x == target_x and y == target_y:
                    break
                mini = 10000000
                for k in range(4):
                    if 1 <= x + dx[k] <= 100 and 1 <= y + dy[k] <= 100 and abs(x + dx[k] - target_x) + abs(
                            y + dy[k] - target_y) < mini:
                        mini = abs(x + dx[k] - target_x) + abs(y + dx[k] - target_y)
                        dir = k
                q.append([x + dx[dir], y + dy[dir]])
                res.append([x + dx[dir], y + dy[dir]])
        l = max(l, len(res))
        a.append(res)

    cnt = []
    for i in range(l):
        for j in range(len(a)):
            for k in range(j + 1, len(a)):
                if i < len(a[j]) and i < len(a[k]) and a[j][i][0] == a[k][i][0] and a[j][i][1] == a[k][i][1] and [
                    a[j][i][0], a[j][i][1]] not in cnt:
                    cnt.append([a[j][i][0], a[j][i][1]])

    answer = len(cnt)
    return answer

solution([[3, 2], [6, 4], [4, 7], [1, 4]]	,[[4, 2], [1, 3], [2, 4]]	)