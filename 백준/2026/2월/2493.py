n = int(input())  # 50만
arr = list(map(int, input().split()))

stack = []  # (num, idx) 로 넣기
for idx, num in enumerate(arr):
    while stack and stack[-1][0] < num:
        stack.pop()
    if not stack:
        print(0, end=' ')
    else:
        print(stack[-1][1], end=' ')
    stack.append((num, idx+1))