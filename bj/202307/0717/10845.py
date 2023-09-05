N = int(input())

queue = list()
order = list()
empty_ = []

for i in range(0,N):
    order.append(input())

for i in range(0,N):
    if order[i].split()[0] == 'push':
        queue.append(int(order[i].split()[1]))
    elif order[i] == 'pop':
        if queue == empty_:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
    elif order[i] == 'size':
        print(len(queue))
    elif order[i] == 'empty':
        if queue == empty_:
            print(1)
        else:
            print(0)
    elif order[i] == 'front':
        if queue == empty_:
            print(-1)
        else:
            print(queue[0])
    else:
        if queue == empty_:
            print(-1)
        else:
            print(queue[-1])