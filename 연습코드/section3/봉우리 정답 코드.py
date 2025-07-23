n = int(input())
arr = [[0] * (n+2)]
for i in range(1, n+1):
    arr.append(list(map(int, input().split())))
    arr[i].append(0)
    arr[i].insert(0,0)
arr.append([0] * (n+2))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
for x in range(1, n+1):
    for y in range(1, n+1):
        if all(arr[x][y] > arr[x+dx[k]][y+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)