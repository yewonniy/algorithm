import sys
sys.setrecursionlimit(10000000)
arr = list(map(int, input().split()))  # [1, 2, 2, 4, 0]
arr.pop()

connect = [[1, 2, 3, 4], [2, 4], [1, 3], [2, 4], [1, 3]]

mini = 4000000


def dfs(level, pos, cnt):
    global mini
    if level == len(arr):
        mini = min(mini, cnt)
        return
    if cnt > mini:
        return
    if pos[1] == arr[level]:
        dfs(level+1, [pos[0], arr[level]], cnt + 1)
    elif pos[1] == 0:
        dfs(level + 1, [pos[0], arr[level]], cnt + 2)
    elif arr[level] in connect[pos[1]]:
        dfs(level + 1, [pos[0], arr[level]], cnt + 3)
    else:
        dfs(level + 1, [pos[0], arr[level]], cnt + 4)
    if pos[0] == arr[level]:
        dfs(level+1, [arr[level], pos[1]], cnt + 1)
    elif pos[0] == 0:
        dfs(level+1, [arr[level], pos[1]], cnt + 2)
    elif arr[level] in connect[pos[0]]:
        dfs(level+1, [arr[level], pos[1]], cnt + 3)
    else:
        dfs(level + 1, [arr[level], pos[1]], cnt + 4)


dfs(1, [arr[0], 0], 2)
print(mini)