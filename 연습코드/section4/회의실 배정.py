n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(reverse=True)

cnt = 1
use = [arr[0]]
for i in range(n-1):
    if arr[i+1][1] <= use[-1][0]: # 전 회의 끝 시간
        cnt += 1
        use.append(arr[i+1])

print(cnt)


# 끝나는 시간이 가장 빠른 회의부터 (이게 정석)
arr.sort(key=lambda x: x[1])
cnt = 1
end =  arr[0][1]
for i in range(1,n):
    if arr[i][0] >= end:
        cnt += 1
        end = arr[i][1]
print(cnt)
