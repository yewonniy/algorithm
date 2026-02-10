import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1], x[0]))

end = arr[0][1]
cnt = 1

for i in range(1,n):
    if arr[i][0] >= end:
        cnt += 1
        end = arr[i][1]
print(cnt)