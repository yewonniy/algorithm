from bisect import bisect_left
n = int(input())
arr = list(map(int, input().split())) # 결국 이 문제도 arr에서 최대 증가 수열을 찾으라는 것. 완전 LIS 그 자체
lis = [arr[0]]

for x in arr:
    if x > lis[-1]:
        lis.append(x)
    else:
        index = bisect_left(lis, x)
        lis[index] = x

print(len(lis))