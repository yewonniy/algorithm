arr = list(input())

stack = [arr[0], arr[1]]

popped_math = arr[1]
for i in range(2, len(arr)):
    if arr[i].isdigit():
        if len(stack) > 0 and not (stack[-1].isdigit()):
            popped_math = stack.pop()
            stack.append(arr[i])
        else:
            stack.append(arr[i])
            stack.append(now)
    else:
        if popped_math == "+" or popped_math == "-":
            now = arr[i]