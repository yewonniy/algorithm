n = int(input())
spr = []
for i in range(0, n):
    spr.append(-1)


def sprinkle(num):
    if check(num):
        if n == num:
            print(spr)
        else:
            for j in range(0, n):
                spr[num] = j
                sprinkle(num+1)


def check(num):
    for k in range(0, num-1):
        if spr[num-1] == spr[k]:
            return False
        elif (abs(spr[num-1]-spr[k])) == (num-1-k): # 대각선, spr[num-1]은 방금 막 넣어본 것, spr[k]는 이미 넣어져 있던 것
            return False
    return True


sprinkle(0)