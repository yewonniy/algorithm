n= int(input())
arr = list(map(int, input().split()))
arr.sort()
res = 0
for i in range(n):
    res += arr[i] * (n-i)
print(res)