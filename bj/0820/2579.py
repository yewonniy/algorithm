import sys
n = int(input())

step = []
for i in range(n):
    step.append(int(sys.stdin.readline().rstrip()))

max_ = 0
memo = []
step.reverse()

i = 0
cur = 0
while i < n:
    cur += step[i]
    memo.append(i)
    if len(memo) > 1 and memo[-1] - memo[-2] == 1:
        i += 2
    else:
        if i < n-2:
            if step[i + 1] > step[i + 2]:
                i += 1
            else:
                i += 2
        else:
            i += 1

print(cur)