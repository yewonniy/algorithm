k = int(input())
arr = list(map(int, input().split()))
ch = [0] * (sum(arr) + 1)


def dfs(L, res):
    if L == k:
        if res > 0:
            ch[res] = 1
        return
    n = arr[L]  # 얘를 +, -, 안씀 중에 하나로
    dfs(L + 1, res + n)
    dfs(L + 1, res - n)
    dfs(L + 1, res)


dfs(0, 0)
print(ch.count(0) - 1)
