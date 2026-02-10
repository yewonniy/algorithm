n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

res = 0
for i in range(n):
    x = arr[i] - b
    cnt = 1
    if x > 0:
        cnt += (x//c)
        if x % c > 0:
            cnt += 1
    res += cnt

print(res)