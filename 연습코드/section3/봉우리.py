n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

cnt = 0
for x in range(n):
    for y in range(n):
        if x == 0 and y == 0: # [0][0]
            maxi = max(arr[1][0], arr[0][1])
        elif x == 0: # 0번째 열
            if y == n-1: # [0][n-1]
                maxi = max(arr[x][y-1], arr[x+1][y])
            else:
                maxi = max(arr[x][y+1], arr[x][y-1], arr[x+1][y])
        elif y == 0: # 0번째 행
            if x == n-1: # 마지막 열 0번째 행
                maxi = max(arr[x][y + 1], arr[x-1][y])
            else:
                maxi = max(arr[x][y + 1], arr[x-1][y], arr[x + 1][y])
        elif x == n-1: # 마지막 열
            if y == n-1:
                maxi = max(arr[x][y - 1], arr[x - 1][y])
            else:
                maxi = max(arr[x][y + 1], arr[x][y - 1], arr[x - 1][y])
        elif y == n-1: # 마지막 행
            maxi = max(arr[x][y - 1], arr[x-1][y], arr[x + 1][y])
        else:
            maxi = max(arr[x][y + 1], arr[x][y - 1], arr[x + 1][y], arr[x -1][y])
        if maxi < arr[x][y]:
            cnt += 1
print(cnt)