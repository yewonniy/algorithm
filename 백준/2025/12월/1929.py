m,n = map(int, input().split())
is_prime = [True for i in range(n+1)]
is_prime[0], is_prime[1] = False, False
# 에라토스테네스의 체
# 2부터 배수들 다 지워

for i in range(2, int((n+1)**0.5)+1):
    for j in range(2, (n+1)//i+1):
        if i*j <= n:
            is_prime[i*j] = False
for i in range(m, n+1):
    if is_prime[i]:
        print(i)