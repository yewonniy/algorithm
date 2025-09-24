def solution(number, k):
    stack = [int(number[0])]
    popped = 0
    for i in range(1, len(number)):
        while stack and int(number[i]) > stack[-1]:
            if popped == k:
                break
            stack.pop()
            popped += 1
        stack.append(int(number[i]))
    stack = list(map(str, stack[0:len(number)-k]))
    return ''.join(stack)