stack = []
# pop 되고 나서 stack 안에 남아있는 원소의 갯수를 더하면 됨.
laser = list(input())

cnt = 0
index = -1
for i in range(len(laser)):
    stack.append(laser[i])
    if index != i-1 and len(stack) > 1 and stack[-1] == ")" and stack[-2] == "(":
        stack.pop()
        stack.pop()
        cnt += stack.count('(')
        index = i
        k = stack.count(')')
        if k > 0:
            stack = ["("] * (len(stack)-k*2)

print(cnt+ stack.count('('))