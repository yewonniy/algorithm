n = int(input())
arr = list(map(int, input().split()))
memo = [0] * n
# 1. 현재 idx, 값 = arr[idx]일때,
# 2. for i in range(idx+1, n) 돌면서 arr[idx] < arr[i]이면,
# 3. dfs(i)를 부른다. = "야! 나보다 큰 수인 너! 너에서 시작해서 최대 증가 수열 몇이야?
# 4. 넵 저 최대 증가 수열 길이 k입니다!
# 5. ok. 그럼 나는 1 + max(k)


def dfs(idx):
    if memo[idx] != 0:
        return memo[idx]
    memo[idx] = 1  # 일단 나 자신 1개로 초기화
    k = 0
    for i in range(idx+1, n):
        if arr[i] > arr[idx]:
            k = max(k, dfs(i))
    memo[idx] = 1+k
    return memo[idx]


for i in range(n):
    dfs(i)
print(max(memo))