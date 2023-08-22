n = int(input())

cnt = 1

# i는 2의 갯수
for i in range(1, n//2+1):
    up_ = 1
    down_ = 1
    min_ = min(i, n-2*i)
    max_ = max(i, n-2*i)
    for j in range(max_+1, min_+max_+1):
        up_ *= j
    for k in range(1, min_+1):
        down_ *= k
    cnt += (up_//down_) * (2**i)

print(cnt % 796796)

# 정답
n = int(input())

memo = [0] * (n+1)

memo[1] = 1
memo[2] = 3

for i in range(3, n+1):
    memo[i] = (memo[i-1] + memo[i-2]*2)

print(memo[n] % 10007)