n, k = map(int, input().split()) # 존재할 수 있는 약수의 최대 개수는 2*n**0.5

cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)