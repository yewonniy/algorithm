from collections import deque
depth = 0


def bfs(route, i, points):
    global depth
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append([points[route[i] - 1][0], points[route[i] - 1][1]])
    target_x = points[route[i + 1] - 1][0]
    target_y = points[route[i + 1] - 1][1]
    L = 0
    mini = 100000000
    r = [0, 0]
    res = []
    while q:
        for i in range(len(q)):
            x, y = q.popleft()
            if abs(x - target_x) + abs(y - target_y) < mini:
                mini = abs(x - target_x) + abs(y - target_y)
                r = [x, y]
            if x == target_x and y == target_y:
                depth = max(depth, L)
                res.append([x, y])
                return res
            for j in range(4):
                xx = x + dx[j]
                yy = y + dy[j]
                if 1 <= xx <= 100 and 1 <= yy <= 100:
                    q.append([xx, yy])
        res.append(r)
        L += 1


def solution(points, routes):
    global depth
    a = []
    for i in range(len(routes)):
        temp = []
        route = routes[i]
        for j in range(len(route) - 1):
            if j == 0:
                temp.extend(bfs(route, j, points))
            else:
                temp.extend((bfs(route, j, points))[1::])
        a.append(temp)

    visited = []
    for i in range(depth + 1):
        for j in range(len(a)):
            if len(a[j]) > i:
                x = a[j][i][0]
                y = a[j][i][1]
                for k in range(j + 1, len(a)):
                    if len(a[k]) > i and x == a[k][i][0] and y == a[k][i][1] and [x, y] not in visited:
                        visited.append([x, y])
    answer = len(visited)
    return answer

solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]])