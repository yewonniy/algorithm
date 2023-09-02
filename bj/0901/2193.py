import sys
sys.setrecursionlimit(10000)
N = int(input())
cnt = 0

# 다이나믹 프로그래밍 -> 리스트는 메모리 초과, 리스트 안써도 시간초과
def pin(n):
    global cnt
    if len(str(n)) == N:
        cnt += 1
        return cnt
    if n % 10 == 1:
        n = n*10
        pin(n)
    else:
        n *= 10
        pin(n)
        n += 1
        pin(n)


if N == 1:
    print(1)
else:
    pin(1)
    print(cnt)

# 위에꺼 시간 초과 나서 아래 꺼로
# 아래껀 메모리 초과.. 나네..
N = int(input())


def pinary_(n):
    result = [1, 0]
    for i in range(2, N-1):
        cnt_zero = result.count(0)
        cnt_one = result.count(1)
        result = []
        for k in range(cnt_zero):
            result.append(0)
            result.append(1)
        for j in range(cnt_one):
            result.append(0)
    print(len(result))


if N == 1 or N == 2:
    print(1)
else:
    pinary_(N)

# 재시도 (규칙 찾음)
M = int(input())


def pin_2(n):
    cnt_zero = 1
    cnt_one = 1
    for i in range(3, M):
        temp = cnt_zero
        cnt_zero += cnt_one
        cnt_one = temp
    print(cnt_zero + cnt_one)


if M == 1 or M == 2:
    print(1)
elif M == 3:
    print(2)
else:
    pin_2(M)