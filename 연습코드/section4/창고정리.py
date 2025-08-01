l = int(input()) # 창고 가로 길이
arr = list(map(int, input().split()))
m = int(input())

for i in range(m):
    arr.sort()
    arr[-1] -= 1
    arr[0] += 1

print(max(arr) - min(arr))


