n = int(input()) # 400만
# 2부터 n까지 소수를 구한다.
# 투포인터
is_prime = [True] * (n+1)

for i in range(2, int(n**0.5)+2):
    k = 2
    while i * k <= n:
        is_prime[i*k] = False
        k += 1
arr = []
for i in range(2,n+1):
    if is_prime[i]:
        arr.append(i)
if n == 1: print(0)
elif n == 2 or n == 3: print(1)
else:
    pt1, pt2, tot, res = 0, 0, 0, 0
    # print(arr)
    while True:
        # 종료조건
        if pt1 > pt2:
            break
        if pt2 == len(arr):
            break

        tot += arr[pt2]
        if tot < n:
            pt2 += 1
        elif tot > n:
            tot -= (arr[pt1]+arr[pt2])
            pt1 += 1
        else:
            # print(arr[pt1],"~",arr[pt2])
            res += 1
            tot -= (arr[pt1] + arr[pt2])
            pt1 += 1
    print(res)