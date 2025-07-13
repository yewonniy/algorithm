n, k = map(int, input().split())
cnt = 0

while not(n==1):
    if n % k == 0:
        cnt += 1
        n = n//k
    else:
        n -= 1
        cnt += 1
print(cnt)