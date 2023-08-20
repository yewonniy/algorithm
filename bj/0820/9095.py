import sys
t = int(input())


def count(n):
    result = 0
    memo = set()
    for i in range(0, n // 3 + 1):
        for j in range(0, n // 2 + 1):
            for k in range(0, n+1):
                if 3*i + 2*j + 1*k == n:
                    memo.add((3, i, 2, j, 1, k))
                    memo.add((3, i, 1, k, 2, j))
                    memo.add((2,j, 1, k, 3, i))
                    memo.add((2, j, 3, i, 1, k))
                    memo.add((1, k, 2, j, 3, i))
                    memo.add((1, k, 3, i, 2, j))
    print(memo)
    result = len(memo)
    return result


cnt = 0
for i in range(t):
    N = int(sys.stdin.readline().rstrip())
    cnt = count(N)
    print(cnt)