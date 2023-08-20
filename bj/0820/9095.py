import sys
t = int(input())


def fact(n):
    result = 1
    if n == 0:
        return 1
    else:
        for i in range(n, 1, -1):
            result = result * i
    return result


def count(n):
    result = 0
    for i in range(0, n // 3 + 1):
        for j in range(0, n // 2 + 1):
            for k in range(0, n+1):
                if 3*i + 2*j + 1*k == n:
                    if (i == 0 and j == 0) or (i == 0 and k == 0) or (j ==0 and k == 0):
                        result += 1
                    else:
                        result += (fact(i+j+k)//(fact(i)*fact(k)*fact(j)))
    return result


cnt = 0
for i in range(t):
    N = int(sys.stdin.readline().rstrip())
    cnt = count(N)
    print(cnt)