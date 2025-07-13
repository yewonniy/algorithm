n = int(input())
memo = []


def solution(cnt, m):
    if m == 1:
        memo.append(cnt)
    if m % 3 == 0:
        solution(cnt+1, m//3)
    if m % 2 == 0:
        solution(cnt+1, m//2)
    if m > 1:
        solution(cnt+1, m-1)


solution(0, n)
print(min(memo))