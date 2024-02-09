import sys
sys.setrecursionlimit(10000)
a, b = map(int, input().split())
memo = []
count = 0


def cal(x, y, cnt):
    global memo
    if y == x:
        memo.append(cnt)
    if y % 2 == 0:
        cnt += 1
        print(y // 2, cnt)
        if y//2 >= x:
            cal(x, y // 2, cnt)
    if y > x and (y-1) % 10 == 0:
        cnt += 1
        print((y - 1) // 10, cnt)
        if (y-1)//10 >= x:
            cal(x, (y - 1) // 10, cnt)


cal(a, b, count)

if len(memo) == 0:
    print(-1)
else:
    print(memo[0]+1)