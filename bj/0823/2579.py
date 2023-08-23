import sys
n = int(input())
arr = []

# n은 계단 갯수 (0 ~ n-1)
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.reverse()
print(arr)


def jump(memo, index, k):
    for i in range(k, n):
        if index[-1] - index[-2] == 1: # 무조건 두 칸
            memo[i] = max(memo[i], memo[i-1])
            index[-1] = 2
        else:
            # 두 칸 뛰기
            memo[i] = memo[i-1] + arr[i]
            if i+2 < n:
                if arr[i+1] < arr[i+2]:
                    if memo[i+2] < memo[i] + arr[i+2]:
                        memo[i+2] = memo[i] + arr[i+2]
                        i = i+2
                        index[-1] = 2
                else:
                    if memo[i+1] < memo[i] + arr[i+1]:
                        memo[i+1] = memo[i] + arr[i+1]
                        print(memo[i+1])
                        index[-1] = 1
            else:
                if i+1 < n:
                    memo[i+1] = memo[i] + arr[i+1]


memo1 = [0] * n
# memo[i] -> i번째 계단 까지 최대값
# memo[now] = max(memo[now - 2] + arr[now], memo[now-1]
result = arr[0]
memo1[0] = arr[0]
memo1[1] = arr[0]+arr[1]
jump(memo1, [0, 1], 2)

memo2 = [0] * n
memo2[0] = arr[0]
memo2[1] = arr[0]
memo2[2] = arr[0] + arr[2]
jump(memo2, [0, 2], 3)

print(memo1, memo2)