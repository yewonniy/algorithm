n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

reward = []
for i in range(n):
    idx = 0
    ch = [0] * 7
    for j in range(3):
        ch[arr[i][j]] += 1
    for j in range(1, 7):
        if ch[j] == 1:
            idx = j
        if ch[j] == 3:
            reward.append(10000 + j*1000)
            break
        if ch[j] == 2:
            reward.append(1000 + j*100)
            break
    else:
        reward.append(idx * 100)

print(max(reward))

