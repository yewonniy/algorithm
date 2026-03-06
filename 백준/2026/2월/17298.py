n = int(input())
arr = list(map(int, input().split()))
stack = []
res = [-1] * n
for i, num in enumerate(arr):
    while stack and stack[-1][0] < num:
        x, idx = stack.pop()
        res[idx] = num
    stack.append((num, i))
print(" ".join(map(str, res)))