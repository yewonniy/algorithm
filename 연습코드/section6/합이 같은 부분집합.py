n= int(input())
arr = list(map(int, input().split()))
ch = [0] * n
res =[False]


def DFS(v):
    if v >= n or (v==1 and ch[0]==0):
        cnt1 = 0
        cnt2 = 0
        for i in range(n):
            if ch[i] == 0:
                cnt1 += arr[i]
            else:
                cnt2 += arr[i]
        if cnt1 == cnt2:
            res[0] = True
        return
    ch[v] = 1
    DFS(v+1)
    ch[v] = 0
    DFS(v+1)


DFS(0)
if res[0]:
    print("YES")
else:
    print("NO")