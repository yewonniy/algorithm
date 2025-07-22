n, m = map(int, input().split())
arr = list(map(int, input().split()))

# cnt = 0
# for i in range(0, n):
#     sum = 0
#     for j in range(i, n):
#         sum += arr[j]
#         if sum == m:
#             cnt += 1
#             break

cnt = 0
pt1 = 0
pt2 = -1
res = 0
while True:
    if res < m:
        if pt2 < n-1:
            pt2 += 1
            res += arr[pt2]
        elif pt1 < n-1:
            pt1 += 1
            res -= arr[pt1]
    elif res == m:
        res -= arr[pt1]
        if pt1 < n-1:
            pt1 += 1
        cnt += 1
    else: # res > m:
        res -= arr[pt1]
        if pt1 < n-1:
            pt1 += 1
    if pt1 == n - 1 and pt2 == n - 1:
        if res == m:
            cnt += 1
        break
print(cnt)

# cnt = 0
# pt1 = 0
# pt2 = 0
# res = 0
#
# while True:
#     res = sum(arr[pt1:pt2+1])
#     if res < m and pt2 < n-1:
#         pt2 += 1
#     elif res == m:
#         cnt += 1
#         if pt1 < n-1:
#             pt1 += 1
#     else: # res > m:
#         if pt1 < n-1:
#             pt1 += 1
#     if pt1 == n - 1 and pt2 == n - 1:
#         if res == m:
#             cnt += 1
#         break
#
# print(cnt)