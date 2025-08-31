n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
m = int(input())
res = 600

# L이 사용한 동전 갯수가 됨
def DFS(L, money):
    global res
    if L >= res: # 가지치기
        return
    if money > m:
        return
    if money == m:
        res = min(res, L)
    for x in coins:
        DFS(L+1, money+x)


DFS(0, 0)
print(res)