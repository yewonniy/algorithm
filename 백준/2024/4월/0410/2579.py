# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.

n = int(input())
step = [0]
for i in range(n):
    step.append(int(input()))

memo = [0] * 301
if n >= 1:
    memo[1] = step[1]
if n>=2:
    memo[2] = step[1] + step[2]
if n >= 3:
    memo[3] = max(step[1] + step[3], step[2] + step[3])
if n >= 4:
    for i in range(4, n+1):
        memo[i] = max(memo[i-3] + step[i-1] + step[i], memo[i-2] + step[i])

print(memo[n])

