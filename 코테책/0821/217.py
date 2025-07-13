arr = []


def one(n, cnt):
    global arr
    if n == 1:
        arr.append(cnt)
    if n % 5 == 0:
        one(n//5, cnt+1)
    if n % 3 == 0:
        one(n//3, cnt+1)
    if n % 2 == 0:
        one(n//2, cnt+1)
    if n > 1:
        one(n-1, cnt+1)


one(26, 0)
print(min(arr))
memo = [23847298374]*1000
memo[1] = 0
# memo[n] 값 - n이라는 숫자가 1에 도달할 수 있는 최소 횟수
# memo[1] - 0
for n in range(1, 27):
    memo[n*5] = min(memo[n*5], memo[n]+1)
    memo[n*3] = min(memo[n*3], memo[n]+1)
    memo[n*2] = min(memo[n*2], memo[n]+1)
    memo[n+1] = min(memo[n+1], memo[n]+1)

for i, val in enumerate(memo):
    print(f"{i} 수는 :  최소 {val}")
    if i == 26:
        break
