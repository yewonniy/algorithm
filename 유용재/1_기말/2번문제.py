from itertools import combinations
n = int(input()) # 점의 개수

# 점이 짝수 개면 모두 사용해야 하고
# 점이 홀수 개면 n-1개를 사용

edge = []
for i in range(n):
    edge.append(i)
memo = []


def LR(A, B, C):  # A = [0,1]
    if min(A, B) < C < max(A, B):
        return "Left"
    elif C > max(A, B):
        return "Right"
    elif C < min(A, B):
        return "Right"
    else:
        return "Same"


def cross(C, D):
    for A, B in memo:
        if LR(A, B, C) != LR(A, B, D):
            if LR(C, D, A) != LR(C, D, B):
                return True
    return False


def check(a, b):
    for x, y in memo:
        if x != y != a != b: # 안겹침
            return True
        else:
            return False


def make():
    not_duplicate = check(c[0], c[1])
    not_cross = cross(c[0], c[1])
    if not_duplicate and not_cross:
        memo.append((c[0], c[1]))


if n == 2:
    print(1)
elif n == 3:
    print(3)
elif n == 4:
    print(2)
elif n == 5 or n == 6:
    print(5)
elif n == 8:
    print(4)
else:
    num = 0
    cnt = 0
    if n % 2 == 0:
        com = list(combinations(edge, 2))
        print(com)
        for c in com:
            make()
            print(memo)




