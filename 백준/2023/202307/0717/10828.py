stack = list()
N = int(input())
order = list()
empty_list = []
for i in range(0,N):
    order.append(input())

print(order)

for i in range(0,N):
    if order[i].split()[0] == 'push':
        stack.append(int(order[i].split()[1]))
    elif order[i] == 'pop':
        if stack == empty_list:
            print(-1)
        else:
            print(stack.pop())
    elif order[i] == 'size':
        print(len(stack))
    elif order[i] == 'empty':
        if stack == empty_list:
            print(1)
        else:
            print(0)
    else:
        if stack == empty_list:
            print(-1)
        else:
            print(stack[-1])
