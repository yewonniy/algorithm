arr = list(input())
stack = []

for x in arr:
    if x.isdigit():
        stack.append(int(x))
    else:
        a = stack.pop()
        b = stack.pop()
        if x == "+":
            stack.append(a+b)
        elif x == "-":
            stack.append(b-a)
        elif x == "*":
            stack.append(a*b)
        else:
            stack.append(b//a)
print(stack[0])