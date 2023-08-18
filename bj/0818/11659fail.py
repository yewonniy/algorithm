import sys

n, m = map(int, input().split())
array = list(map(int, input().split()))

sum_memory = []
for _ in range(n):
    sum_memory.append([0] * n)

result = []
index = []
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    index.append((i-1, j-1))

for i, j in index:
    res = 0
    k = j
    while i <= k:
        if sum_memory[i][k] == 0:
            res += array[k]
            k -= 1
        else:
            res += sum_memory[i][k]
            sum_memory[i][j] = res
            break
    result.append(sum_memory[i][j])

for x in result:
    print(x)