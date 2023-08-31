n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(0, n):
    sum_ = 0
    for j in range(i, n):
        sum_ += arr[j]
        if sum_ == m:
            cnt += 1
            break

print(cnt)