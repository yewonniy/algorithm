n = int(input())


def DFS(v, res):
    if v > n:
        print(res)
        return
    DFS(v+1, res+str(v)+" ")
    DFS(v+1, res)


DFS(1, "")