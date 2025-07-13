import sys
r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(sys.stdin.readline()))
maxi = -1
check = [False] * 26  # A ~ Z까지 총 26개의 알파벳


def dfs(x, y, cnt):
    global maxi
    check[ord(arr[x][y]) - ord("A")] = True  # True면 이미 지난 거
    if x + 1 < r and (not check[ord(arr[x+1][y]) - ord("A")]):
        # 그 칸으로 가기
        dfs(x+1, y, cnt+1)
        check[ord(arr[x + 1][y]) - ord("A")] = False # 원상 복구
    if x - 1 >= 0 and (not check[ord(arr[x-1][y]) - ord("A")]):
        dfs(x-1, y, cnt+1)
        check[ord(arr[x - 1][y]) - ord("A")] = False
    if y+1 < c and (not check[ord(arr[x][y+1]) - ord("A")]):
        dfs(x, y+1, cnt+1)
        check[ord(arr[x][y + 1]) - ord("A")] = False
    if y-1 >= 0 and (not check[ord(arr[x][y-1]) - ord("A")]):
        dfs(x, y-1, cnt+1)
        check[ord(arr[x][y - 1]) - ord("A")] = False
    maxi = max(cnt, maxi)


dfs(0, 0, 1)
print(maxi)