str1 = input()  # 길이: 1 ~ 1,000,000
bomb = list(input())  # 길이: 1 ~ 36
# stack
stack = []
for i in range(len(str1)):
    stack.append(str1[i])
    if len(stack) >= len(bomb):
        ch = 0
        for j in range(-len(bomb), 0, 1):
            if stack[j] == bomb[j + len(bomb)]:
                ch += 1
            else:
                break
        if ch == len(bomb):
            for _ in range(ch):
                stack.pop()

if len(stack) > 0:
    for x in stack:
        print(x, end='')
else:
    print("FRULA")