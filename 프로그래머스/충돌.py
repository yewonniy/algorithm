def solution(points, routes):
    answer = 0
    dic = dict()
    route = []
    for r in routes:
        x = points[r[0] - 1][0]
        y = points[r[0] - 1][1]
        route.append([x, y, r[1::]])
        dic[(x, y, 0)] = dic.get((x, y, 0), 0) + 1

    for i in range(len(route)):
        sx, sy, next_list = route[i]
        k = 1
        for j in range(len(next_list)):
            nx, ny = points[next_list[j] - 1][0], points[next_list[j] - 1][1]
            while True:
                if nx - sx > 0:
                    sx += 1
                elif sx - nx > 0:
                    sx -= 1
                elif ny - sy > 0:
                    sy += 1
                elif sy - ny > 0:
                    sy -= 1
                else:
                    break
                dic[(sx, sy, k)] = dic.get((sx, sy, k), 0) + 1
                k += 1
    for x in dic.values():
        if x > 1:
            answer += 1
    return answer