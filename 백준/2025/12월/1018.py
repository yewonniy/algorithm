# M * N (8 ~ 50)
def cal(l): # l : list
    bw = ["B","W"]
    res = [0,0] # res[0] = "BWBW...", res[1] = "WBWB..."
    for idx, arr in enumerate(l):
        cnt1 = 0
        cnt2 = 0
        for i in range(len(arr)):
            if bw[i%2] == arr[i]:
                cnt2 += 1
            else:
                cnt1 += 1
        if idx%2 == 0:
            res[0] += cnt1
            res[1] += cnt2
        else:
            res[0] += cnt2
            res[1] += cnt1
    return res


n, m = map(int, input().split()) # n이 세로, m이 가로
arr = []
for _ in range(n):
    arr.append(list(input()))

ans = 10**8
for j in range(m - 7):  # j = 0 ~ m-8
    for i in range(n - 7): # i = 0 ~ n-8
        # for k in range(i, i+8): # k = i ~ i+7
        target = []
        for k in range(i, i+8):
            target.append(arr[k][j:j+8])
        res = cal(target)
        ans = min(ans, res[0], res[1])
print(ans)
